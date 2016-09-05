import re

from relation import relation, relationData
from supportedRelations import listeRelation

UNIVERSAL = re.compile(r'.*')
S_GDP = re.compile(r'.*\'s.*gdp.*(was|is|(account.*for)|impicture|worth)')
S_GDP_MORE = re.compile(r'.*\'s.*gdp.*(was|is|(account.*for)|impicture|worth).*(more)')
S_GDP_LESS = re.compile(r'.*\'s.*gdp.*(was|is|(account.*for)|impicture|worth).*(less)')
GDP_IN = re.compile(r'.*gdp.*(in|of).*')
IS = re.compile(r'.*(was|is|(account.*for)|impicture|worth).*')
IS_MORE = re.compile(r'.*(was|is|(account.*for)|impicture|worth).*(((more|greater).*than)|(superior.*to))')
IS_LESS = re.compile(r'.*(was|is|(account.*for)|impicture|worth).*(((less|shorter).*than)|(inferior.*to)).*')


number_dic = {
    'billion': '000000000',
    'million': '000000',
    'thousand': '000',
    'hundread': '00'
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
    text = [replace_int(x) for x in text.split('_')]
    return("".join(text))

hasGDP = relation('hasGDP' , 'GPE' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': S_GDP_MORE, 'comparator': 'more', 'inverted': True},
    {'left': GDP_IN, 'middle': IS_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_GDP_LESS, 'comparator': 'less', 'inverted': True},
    {'left': GDP_IN, 'middle': IS_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_GDP, 'comparator': 'egal', 'inverted': True},
    {'left': GDP_IN, 'middle': IS, 'comparator': 'egal', 'inverted': True},
])

listeRelation.append(hasGDP)
