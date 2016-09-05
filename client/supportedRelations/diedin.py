import re

from relation import relation, relationData
from supportedRelations import listeRelation

UNIVERSAL = re.compile(r'.*')
DIED_IN = re.compile(r'.*\bdied\b.*in.*')

def make_nice(x):
    return x

diedIn = relation('diedIn' , 'PERSON' , 'GPE' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': DIED_IN, 'comparator': 'egal'}
])

listeRelation.append(diedIn)
