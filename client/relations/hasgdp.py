from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
S_GDP = re.compile(r'.*\'s.*\bGDP.*\b(was|is|(account for)|impicture|worth)')
GDP_IN=re.compile(r'.*GDP.*\bin.*')
IS=re.compile(r'.*(was|is|(account for)|impicture|worth)')

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
    {'left': UNIVERSAL, 'middle': S_GDP, 'comparator': 'egal'},
    {'left': GDP_IN, 'middle': IS, 'comparator': 'egal'}
])
