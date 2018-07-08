#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import unittest

FST = '../fst/guesser.fst'

class NounTests(unittest.TestCase):

    def _get_analyses(self, token):
        pipe = Popen(['flookup', '-x', FST], stdout=PIPE, stdin=PIPE)
        analyses, _ = pipe.communicate(input=token.encode('utf-8'))
        return set(analyses.decode('utf-8').strip().split('\n'))

    def test_janataavata(self):
        self.assertEqual(self._get_analyses('ජනතාවට'), {'ජනතාව+N+Dat+Sg'})

    # def test_minisaagee(self):
    #     self.assertEqual(self._get_analyses('මිනිසාගේ'), {'මිනිසා+N+GenLoc+Sg+Anim'})

    def test_sanggamyee(self):
        self.assertEqual(self._get_analyses('සංගමයේ'), {'සංගමය+N+GenLoc+Sg+Inanim'})

    def test_paksaya(self):
        self.assertEqual(self._get_analyses('පක්ෂය'), {'පක්ෂය+N+Nom+Sg'})

    def test_paksayee(self):
        self.assertEqual(self._get_analyses('පක්ෂයේ'), {'පක්ෂය+N+GenLoc+Sg+Inanim'})

    def test_paksayen(self):
        self.assertEqual(self._get_analyses('පක්ෂයෙන්'), {'පක්ෂය+N+InstrAbl+Sg+Inanim'})

    def test_pota(self):
        self.assertEqual(self._get_analyses('පොත'), {'පොත+N+Nom+Sg'})

    def test_potee(self):
        self.assertEqual(self._get_analyses('පොතේ'), {'පොත+N+GenLoc+Sg+Inanim'})

    def test_poten(self):
        self.assertEqual(self._get_analyses('පොතෙන්'), {'පොත+N+InstrAbl+Sg+Inanim'})

    def test_ballaa(self):
        self.assertEqual(self._get_analyses('බල්ලා'), {'බල්ලා+N+Nom+Sg'})

    def test_ballaata(self):
        self.assertEqual(self._get_analyses('බල්ලාට'), {'බල්ලා+N+Dat+Sg'})

    def test_ballaagee(self):
        self.assertEqual(self._get_analyses('බල්ලාගේ'), {'බල්ලා+N+GenLoc+Sg+Anim'})

    def test_ballanwa(self):
        self.assertEqual(self._get_analyses('බල්ලන්ව'), {'බල්ලා+N+Acc+Pl+Anim', 'බල්ල+N+Acc+Pl+Anim'})

    def test_ballangen(self):
        self.assertEqual(self._get_analyses('බල්ලන්ගෙන්'), {'බල්ලා+N+InstrAbl+Pl+Anim', 'බල්ල+N+InstrAbl+Pl+Anim'})

    # def test_ballekugee(self):
    #     self.assertEqual(self._get_analyses('බල්ලෙකුගේ'), {'බල්ලා+N+Indef+GenLoc+Sg'})

    # def test_ballek(self):
    #     self.assertEqual(self._get_analyses('බල්ලෙක්'), {'බල්ලා+N+Nom+Indef+sg'})

    # def test_ballekuta(self):
    #     self.assertEqual(self._get_analyses('බල්ලෙකුට'), {'බල්ලා+N+Indef+Dat+Sg'})

    # def test_ballekuɡen(self):
    #     self.assertEqual(self._get_analyses('බල්ලෙකුගෙන්'), {'බල්ලා+N+Indef+InstrAbl+Sg'})

    def test_ballan(self):
        self.assertEqual(self._get_analyses('බල්ලන්'), {'බල්ලා+N+Nom+Pl+Anim', 'බල්ල+N+Nom+Pl+Anim'})

    def test_balloo(self):
        self.assertEqual(self._get_analyses('බල්ලෝ'), {'බල්ලා+N+Nom+Pl+Anim', 'බල්ල+N+Nom+Pl+Anim'})

    def test_ballanta(self):
        self.assertEqual(self._get_analyses('බල්ලන්ට'), {'බල්ලා+N+Dat+Pl+Anim', 'බල්ල+N+Dat+Pl+Anim'})

    def test_ballangee(self):
        self.assertEqual(self._get_analyses('බල්ලන්ගේ'), {'බල්ලා+N+GenLoc+Pl+Anim', 'බල්ල+N+GenLoc+Pl+Anim'})

    def test_ballanwa(self):
        self.assertEqual(self._get_analyses('බල්ලන්ව'), {'බල්ලා+N+Acc+Pl+Anim', 'බල්ල+N+Acc+Pl+Anim'})

    def test_kolamba(self):
        self.assertEqual(self._get_analyses('කොළඹ'), {'කොළඹ+N+Nom+Sg'})

    def test_kolambata(self):
        self.assertEqual(self._get_analyses('කොළඹට'), {'කොළඹ+N+Dat+Sg'})

    def test_kolambin(self):
        self.assertEqual(self._get_analyses('කොළඹින්'), {'කොළඹ+N+InstrAbl+Sg+Inanim'})

    def test_kaantaava(self):
        self.assertEqual(self._get_analyses('කාන්තාව'), {'කාන්තාව+N+Nom+Sg'})

    def test_kaantaavagen(self):
        self.assertEqual(self._get_analyses('කාන්තාවගෙන්'), {'කාන්තාව+N+InstrAbl+Sg+Anim'})

    def test_kaantaavata(self):
        self.assertEqual(self._get_analyses('කාන්තාවට'), {'කාන්තාව+N+Dat+Sg'})

    def test_kaantaavagee(self):
        self.assertEqual(self._get_analyses('කාන්තාවගේ'), {'කාන්තාව+N+GenLoc+Sg+Anim'})

    def test_kaantaavan(self):
        self.assertEqual(self._get_analyses('කාන්තාවන්'), {'කාන්තාව+N+Nom+Pl+Anim'})

    def test_kaantaavanɡee(self):
        self.assertEqual(self._get_analyses('කාන්තාවන්ගේ'), {'කාන්තාව+N+GenLoc+Pl+Anim'})

    def test_kaantaavanɡen(self):
        self.assertEqual(self._get_analyses('කාන්තාවන්ගෙන්'), {'කාන්තාව+N+InstrAbl+Pl+Anim'})

    def test_kaantavanta(self):
        self.assertEqual(self._get_analyses('කාන්තාවන්ට'), {'කාන්තාව+N+Dat+Pl+Anim'})

    def test_langkaava(self):
        self.assertEqual(self._get_analyses('ලංකාව'), {'ලංකාව+N+Nom+Sg'})

    def test_langkaavee(self):
        self.assertEqual(self._get_analyses('ලංකාවේ'), {'ලංකාව+N+GenLoc+Sg'})

    def test_langkaaven(self):
        self.assertEqual(self._get_analyses('ලංකාවෙන්'), {'ලංකාව+N+InstrAbl+Sg+Inanim'})

    def test_langkaavata(self):
        self.assertEqual(self._get_analyses('ලංකාවට'), {'ලංකාව+N+Dat+Sg'})

    def test_(self):
        self.assertEqual(self._get_analyses(''), {''})

