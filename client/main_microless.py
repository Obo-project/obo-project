from server import post_request
import speech_recognition as sr

import nltk
import re
import hasPopulation
from rel_extract_obo import precompute
from relation import relation, relationData


UNIVERSAL = re.compile(r'.*')
LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is).*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is))')
IN = re.compile(r'\bin\b')

sents = "There are 65 million people in Germany."
sents = precompute(sents)

hasPop = relation('hasPopulation' , 'PPCD' , 'LOC' , patterns={'left':THERE, 'middle': IN})

relations = hasPop.extract(sents)

for rel in relations:
    rel.post()
