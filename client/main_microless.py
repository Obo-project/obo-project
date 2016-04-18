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

sents = "There are 65 million people in Germany."
sents = precompute(sents)
print(sents)


relations = hasPop.extract(sents)
print(relations)

for rel in relations:
    rel.post()
