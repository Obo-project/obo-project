import re

from relation import relation, relationData
from supportedRelations import listeRelation

UNIVERSAL = re.compile(r'.*')
BORN_IN = re.compile(r'.*\bborn\b.*in.*')
BORN_ON = re.compile(r'.*\bborn\b.*on.*')

def make_nice(x):
    return x

bornOnDate = relation('bornOnDate' , 'PERSON' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': BORN_IN, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': BORN_ON, 'comparator': 'egal'}
])

listeRelation.append(bornOnDate)
