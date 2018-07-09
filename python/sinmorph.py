"""Interface to a Foma morphological analyzer for Sinhala.

The API for sinmorph is somewhat different than that of kinmorph. Instead of
passing in a single token on each call, you pass in a list of tokens (thought
this list can, of course, be of length one). This will allow for greater
computational efficiency as Foma will only have to load the FSTs into memory
once per batch. In general, sinmorph should also be faster because of how
it is structureds.

Currently sinmorph only analyzes nouns and only analyzes inflectional
morphology. This should be appropriate for some information extraction tasks
like NER. When a stem is not listed in the lexicon and is inferred, the
property "Guess" is added to the analysis. For some applications, it may be
appropriate to filter this out.

Sample usage:

>>> import sinmorph
>>> smorph = sinmorph.SinMorph(fst='../fst/sinmorph.fst')
>>> smorph.get_lemmas(['ෆෝල්ඩරය'])
['ෆෝල්ඩරය']
>>> smorph.get_morphs(['ෆෝල්ඩරය'])
[['ෆෝල්ඩරය', 'N', 'Nom', 'Sg']]
>>>
"""

from subprocess import Popen, PIPE
import regex as re

class SinMorph(object):
    """Interface to the sinmorph.fst via Foma."""

    def __init__(self, fst='../fst/sinmorph.fst'):
        """Construct a SinMorph object.

        Args:
           fst (str): Path to a compiled FST file for FOMA including FSTs
           for attested and guessed tokens. This should probably be
           'sinmorph.fst'
        """
        self.fst = fst

    def _get_cost(self, ana_morph_lemma):
        analysis, morphs, lemma = ana_morph_lemma
        cost = 0
        if 'Voc' in morphs:
            cost += 1
        if len(lemma) < 3:
            cost += 2
        if len(lemma) < 1:
            cost += 10
        return cost

    def _to_morphs(self, analysis):
        try:
            return analysis[1:].split('+')
        except IndexError:
            return []

    def _get_lemma(self, morphs):
        try:
            return [m for m in morphs
                    if re.match('^[a-z\u200d\p{Sinhala}]+$', m)][0]
        except IndexError:
            return ''

    def _get_best_analysis(self, analyses):
        morph_list = [x.split('+') for x in analyses]
        lemma_list = [self._get_lemma(x) for x in morph_list]
        costs = map(self._get_cost, zip(analyses, morph_list, lemma_list))
        try:
            _, morphs, lemma = sorted(zip(costs, morph_list, lemma_list))[-1]
            return (morphs, lemma)
        except IndexError:
            return (None, None)

    def _get_analyses(self, tokens):
        tokens = [t.replace('\u200d', '') for t in tokens]
        token_list = '\n'.join(tokens)
        pipe = Popen(['flookup', '-a', '-x', self.fst],
                     stdout=PIPE, stdin=PIPE)
        analyses, resp = pipe.communicate(input=token_list.encode('utf-8'))
        analyses = analyses.decode('utf-8').strip()
        analysis_list = []
        for token, token_analyses in zip(tokens, analyses.split('\n\n')):
            morphs, lemma = self._get_best_analysis(token_analyses.split('\n'))
            if lemma:
                analysis_list.append((morphs, lemma))
            else:
                analysis_list.append(([token], token))
        return zip(token_list, analysis_list)

    def get_lemmas(self, tokens):
        """Return list of lemmas, one per token.

        Args:
            tokens (list): a list of strings each of which is a Sinhala word

        Returns (list):
            A list of strings, each of which is the hypothesized lemma for the
            corresponding tokens
        """
        return [l for (_, (m, l)) in self._get_analyses(tokens)]

    def get_morphs(self, tokens):
        """Return list of morpheme lists, one per token.

        Args:
            tokens(list): a list of strings each of which is a Sinhala word

        Returns (list):
            a list of lists of strings. Each list consists of the hypothesized
            morphological properties of the corresponding word
        """
        return [m for (_, (m, l)) in self._get_analyses(tokens)]
