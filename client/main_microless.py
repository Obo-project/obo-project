from server import post_request
import speech_recognition as sr

import nltk
import re
from rel_extract_obo import precompute
from relations.hasPop import *


UNIVERSAL = re.compile(r'.*')
LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is).*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is))')
IN = re.compile(r'\bin\b')

sents = "There are more than 65 million people in France."
print("Analysed sentence : ", sents)
sents = precompute(sents)
print("Precomputed sentence : ", sents)

relations = hasPop.extract(sents)

for rel in relations:
    rel.post()
