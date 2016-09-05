import re

from relation import relation, relationData
from supportedRelations import listeRelation, grammar, dic

UNIVERSAL = re.compile(r'.*')
LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is|living)+.*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is))+\b(?!.+than)')
THERE_MORE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is)).*(((more|greater).*than)|(superior.*to))')
THERE_LESS = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is)).*(((less|shorter).*than)|(inferior.*to))')
IN = re.compile(r'.*\bin\b(?!\b.+ing)')

number_dic = {
    'billion': '000000000',
    'million': '000000',
    'thousand': '000',
    'hundread': '00'
}

haspop_grammar = "CDD: {<CD>*} \nPPCD: {<CDD><PPUNIT>}"

haspop_dic = {
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

hasPopulation = relation('hasPopulation' , 'PPCD' , 'GPE' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': LIVE_IN, 'comparator': 'egal'},
    {'left': THERE, 'middle': IN, 'comparator': 'egal'},
    {'left': THERE_MORE, 'middle': IN, 'comparator': 'more'},
    {'left': THERE_LESS, 'middle': IN, 'comparator': 'less'}
])

listeRelation.append(hasPopulation)
dic.update(haspop_dic)
grammar.append(haspop_grammar)
