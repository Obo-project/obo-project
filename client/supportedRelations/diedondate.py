import re

from relation import relation, relationData
from supportedRelations import listeRelation

UNIVERSAL = re.compile(r'.*')
DIED_IN = re.compile(r'.*\bdied\b.*in.*')
DIED_ON=re.compile(r'.*\bdied\b.*on.*')

def make_nice(x):
    return x

diedOnDate = relation('diedOnDate' , 'PERSON' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': DIED_IN, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': DIED_ON, 'comparator': 'egal'}
])

listeRelation.append(diedOnDate)
