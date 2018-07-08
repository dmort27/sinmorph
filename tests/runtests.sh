#!/bin/sh

cd ../fst
foma -l sinmorph.xfst -s
cd ../tests
python -m unittest
