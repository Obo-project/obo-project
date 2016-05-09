from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
DIED_IN = re.compile(r'.*\bdied\b.*in.*')

def make_nice(x):
    return x

diedIn = relation('diedIn' , 'PERSON' , 'GPE' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': DIED_IN, 'comparator': 'egal'}
])