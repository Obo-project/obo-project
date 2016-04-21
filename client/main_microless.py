from server import post_request
import speech_recognition as sr

import nltk
import re
from precompute import precompute
from relations import listeRelation

sents = "There are more than 10 million people in France."
print("Analysed sentence : ", sents)
sents = precompute(sents)
#print("Precomputed sentence : ", sents)

for relation in listeRelation:
    rels = relation.extract(sents)

    for rel in rels:
        rel.post();
