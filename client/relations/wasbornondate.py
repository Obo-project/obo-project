from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
BORN_IN = re.compile(r'.*\bborn\b.*in.*')
BORN_ON = re.compile(r'.*\bborn\b.*on.*')

def make_nice(x):
    return x

bornOnDate = relation('bornOnDate' , 'PERSON' , 'DATE' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': BORN_IN, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': BORN_ON, 'comparator': 'egal'}
])
