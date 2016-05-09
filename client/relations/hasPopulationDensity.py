from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
IS = re.compile(r'.*\bis\b')
HAS_POPULATION_DENSITY = re.compile(r'.*has.*population\bdensity.*')
S_POPULATION_DENSITY = re.compile(r'.*\'s\bis.*\bdensity\b.*of.*')
POPULATION_DENSITY_OF = re.compile(r'.*population\b.*density.*of.*')
THERE_ARE = re.compile(r'.*(There\bare|There\'re|there\bare|there\'re)')
IN= re.compile(r'.*in')


number_dic = {
    'billion': '000000000',
    'million': '000000',
    'thousand': '000',
    'hundread': '00'
}

dic = {
    "square": "AREA",
    "kilometer": "AREA",
    "kilometre": "AREA",
    "per": "PER"
}

def replace_int(x):
    try:
        int(x)
        return x
    except ValueError:
        if(x in number_dic.keys()):
            return number_dic[x]
        else:
            return x;

def make_nice(text):
    text = [replace_int(x) for x in text.split('_')]
    return(" ".join(text))

grammar = """
    PPDENSITY: {<CD>+<PPUNIT><PER><AREA>+}"""

hasPopulationDensity = relation('hasPopulationDensity' , 'GPE' , 'PPDENSITY' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': HAS_POPULATION_DENSITY, 'comparator': 'egal'},
    {'left': S_POPULATION_DENSITY, 'middle': IS, 'comparator': 'egal'},
    {'left': POPULATION_DENSITY_OF, 'middle': IS, 'comparator': 'egal'},
])
