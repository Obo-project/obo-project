from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
CAPITAL_OF = re.compile(r'.*\bcapital\b.*of.*')

def make_nice(x):
    return x

hasCapital = relation('capitalOf' , 'GPE' , 'GPE' , make_nice , patterns_list=[
    {'left':UNIVERSAL , 'middle': CAPITAL_OF , 'comparator': 'egal'}])
