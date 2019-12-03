#!/bin/bash
for (( i=5; i>=1; i-- ))
do 
	python ASR.py
	./mt.sh
	python jsontotxt.py
	cat mtresult.txt
	python TTS.py
done