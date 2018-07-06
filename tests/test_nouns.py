#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import unittest

FST = '../fst/sinmorph.fst'

class NounTests(unittest.TestCase):

    def _get_analyses(self, token):
        pipe = Popen(['flookup', '-x', FST], stdout=PIPE, stdin=PIPE)
        analyses, _ = pipe.communicate(input=token.encode('utf-8'))
        return set(analyses.decode('utf-8').strip().split('\n'))

    def test_janataavata(self):
        self.assertEqual(self._get_analyses('ජනතාවට'), {'ජනතාව+N+Dat+Sg'})

    def test_minisaagee(self):
        self.assertEqual(self._get_analyses('මිනිසාගේ'), {'මිනිසා+N+GenLoc+Sg+Anim'})

    def test_sanggamyee(self):
        self.assertEqual(self._get_analyses('සංගමයේ'), {'සංගමය+N+GenLoc+Sg+Inanim'})

    def test_paksaya(self):
        self.assertEqual(self._get_analyses('පක්ෂය'), {'පක්ෂය+N+Nom+Sg'})

    def test_paksayee(self):
        self.assertEqual(self._get_analyses('පක්ෂයේ'), {'පක්ෂය+N+GenLoc+Sg+Inanim'})

    def test_paksayen(self):
        self.assertEqual(self._get_analyses('පක්ෂයෙන්'), {'පක්ෂය+N+InstrAbl+Sg+Inanim'})
