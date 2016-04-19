from server import post_request
import speech_recognition as sr

import nltk
import re
from rel_extract_obo import precompute
from relations.hasPop import *

sents = "There are more than 10 million people in France."
print("Analysed sentence : ", sents)
sents = precompute(sents)
print("Precomputed sentence : ", sents)

relations = hasPop.extract(sents)

for rel in relations:
    rel.post();
