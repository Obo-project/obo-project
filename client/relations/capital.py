from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
IS = re.compile(r'.*\bis\b')
CAPITAL_OF = re.compile(r'.*\bcapital\b.*of.*')
IS_CAPITAL_OF = re.compile(r'.*\bis.*\bcapital\b.*of.*')
S_CAPITAL = re.compile(r'.*\'s.*\bcapital.*\bis')

def make_nice(x):
    return x

capital = relation('hasCapital' , 'GPE' , 'GPE' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': IS_CAPITAL_OF, 'comparator': 'egal'},
    {'left': CAPITAL_OF, 'middle': IS, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_CAPITAL, 'comparator': 'egal', 'inverted': True}
])
