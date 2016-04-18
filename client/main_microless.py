from server import post_request
import speech_recognition as sr

import nltk
import re
import hasPopulation
from rel_extract_obo import precompute


UNIVERSAL = re.compile(r'.*')

sents = "There are 65 million people in Germany."
print(sents)
sents = precompute(sents)

hasPopulation.search_rel(sents)
