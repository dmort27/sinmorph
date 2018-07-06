#!/usr/bin/env python3

from subprocess import Popen, PIPE
import unittest

FST = '../fst/sinmorph.fst'

class NounTests(unittest.TestCase):

    def _get_analyses(self, token):
        pipe = Popen(['flookup', '-x', FST], stdout=PIPE, stdin=PIPE)
        analyses, _ = pipe.communicate(input=token.encode('utf-8'))
        return set(analyses.decode('utf-8').strip().split('\n'))

    def test_noun1(self):
        self.assertEqual(self._get_analyses('ජනතාවට'), {'ජනතාව+N+Sg+Dat+Anim'})
