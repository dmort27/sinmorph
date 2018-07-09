#!/usr/bin/env python3

import csv
import sys
import re

def main(fn):
    with open(fn, encoding='utf-8') as f:
        for orth, phon, pos, gloss in csv.reader(f, dialect='excel-tab'):
            if pos == 'NOUN' and re.search('්$', orth):
                print('{} ConsStem; ! {} "{}"'.format(orth[:-1], phon, gloss))

if __name__ == '__main__':
    main(sys.argv[1])
