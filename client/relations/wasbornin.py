from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
BORN_IN = re.compile(r'.*\bborn\b.*in.*')

def make_nice(x):
    return x

bornIn = relation('bornIn' , 'PERSON' , 'GPE' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': BORN_IN, 'comparator': 'egal'}
])
