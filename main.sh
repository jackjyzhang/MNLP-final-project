#!/bin/bash
python ASR.py

./mt.sh

python jsontotxt.py

cat mtresult.txt