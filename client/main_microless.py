from server import post_request
import speech_recognition as sr

import nltk
import re
from precompute import precompute
from relations import listeRelation

# sents = "The capital of France is Paris."
# sents = "France's capital is Paris."
# sents = "France's capital is Palaiseau."
# sents = "Paris is the capital of France."
sents = "There are 70 million people in France."
# sents = "There are more than 10 million people in France."
# sents = "There are less than 10 million people in France."
sents = "John is born in tuesday"

print("Analysed sentence : ", sents)
sents = precompute(sents)
print("Precomputed sentence : ", sents)

for relation in listeRelation:
    rels = relation.extract(sents)

    for rel in rels:
        rel.post();
