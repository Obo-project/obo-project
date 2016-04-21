from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is|living)+.*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is))+\b(?!\b.+than)')
THERE_MORE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is)).*(more.*than)')
THERE_LESS = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is)).*(less.*than)')
IN = re.compile(r'.*\bin\b(?!\b.+ing)')

number_dic = {
    'million': '000000'
}

grammar = """
    CDD: {<CD>*}
    PPCD: {<CDD><PPUNIT>}"""

dic = {
	"people": "PPUNIT",
	"inhabitants": "PPUNIT"
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

hasPop = relation('hasPopulation' , 'PPCD' , 'LOC' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': LIVE_IN, 'comparator': 'egal'},
    {'left': THERE, 'middle': IN, 'comparator': 'egal'},
    {'left': THERE_MORE, 'middle': IN, 'comparator': 'more'},
    {'left': THERE_LESS, 'middle': IN, 'comparator': 'less'}])
