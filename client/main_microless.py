import re

import speech_recognition as sr
import nltk

from server import post_request
from precompute import precompute
from supportedRelations import *
from supportedRelations import listeRelation, dic


# sents = "The capital of France is Paris."
# sents = "France's capital is Paris."
# sents = "France's capital is Palaiseau."
# sents = "Paris is the capital of France."
# sents = "There are 70 million people in France."
# sents = "There are more than 10 million people in France."
# sents = "There are less than 10 million people in France."
# sents = "population density of France is 100 inhabitants per square kilometer"
# sents = "The gdp in France is 10 billion dollars"
# sents = "France's import is 10 billion dollars"
sents = "France has population density greater than 100 people per kilometer square"

print("Analysed sentence : ", sents)
sents = precompute(sents)
print("Precomputed sentence : ", sents)

for relation in listeRelation:
    rels = relation.extract(sents)

    for rel in rels:
        rel.post();
