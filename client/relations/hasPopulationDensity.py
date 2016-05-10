from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
IS = re.compile(r'.*(was|is)')
IS_MORE = re.compile(r'.*(was|is).*(((more|greater).*than)|(superior.*to))')
IS_LESS = re.compile(r'.*(was|is).*(((less|shorter).*than)|(inferior.*to))')
HAS_POPULATION_DENSITY = re.compile(r'.*has.*population.*density.*')
HAS_POPULATION_DENSITY_MORE = re.compile(r'.*has.*population.*density.*(((more|greater).*than)|(superior.*to))')
HAS_POPULATION_DENSITY_LESS = re.compile(r'.*has.*population.*density.*(((less|shorter).*than)|(inferior.*to))')
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
            return "";

def make_nice(text):
    text = [replace_int(x) for x in text.split('_') if replace_int(x) != ""]
    return(" ".join(text))

grammar = """
    PPDENSITY: {<CD>+<PPUNIT><PER><AREA>+}"""

hasPopulationDensity = relation('hasPopulationDensity' , 'GPE' , 'PPDENSITY' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': HAS_POPULATION_DENSITY_MORE, 'comparator': 'more', 'inverted':True},
    {'left': UNIVERSAL, 'middle': HAS_POPULATION_DENSITY_LESS, 'comparator': 'less', 'inverted':True},
    {'left': UNIVERSAL, 'middle': HAS_POPULATION_DENSITY, 'comparator': 'egal', 'inverted':True},
    {'left': S_POPULATION_DENSITY, 'middle': IS_MORE, 'comparator': 'more', 'inverted':True},
    {'left': POPULATION_DENSITY_OF, 'middle': IS_MORE, 'comparator': 'more', 'inverted':True},
    {'left': S_POPULATION_DENSITY, 'middle': IS_LESS, 'comparator': 'less', 'inverted':True},
    {'left': POPULATION_DENSITY_OF, 'middle': IS_LESS, 'comparator': 'less', 'inverted':True},
    {'left': S_POPULATION_DENSITY, 'middle': IS, 'comparator': 'egal', 'inverted':True},
    {'left': POPULATION_DENSITY_OF, 'middle': IS, 'comparator': 'egal', 'inverted':True},
])
