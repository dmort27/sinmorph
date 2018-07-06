#!/usr/bin/env python3

import epitran
import sys

def main(mode):
    epi = epitran.Epitran(mode)
    for line in sys.stdin.buffer:
        print(epi.transliterate(line.strip().decode('utf-8')))

if __name__ == '__main__':
    main(sys.argv[1])
