import nltk
import re
from rel_extract_obo import extract_rels
from server import post_request

UNIVERSAL = re.compile(r'.*')
LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is).*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is))')
IN = re.compile(r'\bin\b')

data = {
    'relation': 'hasPopulation',
    'entity': '',
    'quantity': ''
}

def search_rel(sents):
    relations = []
    for rel in extract_rels('PPCD', 'LOC', sents, patterns={'left': UNIVERSAL, 'middle': LIVE_IN}):
        relations.append(rel)

    for rel in extract_rels('PPCD', 'LOC', sents, patterns={'left': THERE, 'middle': IN}):
        relations.append(rel)

    for r in relations:
        send_rel(r)

def send_rel(rel):
    data['entity'] = make_nice(rel, obj='obj')
    data['quantity'] = make_nice(rel, obj='subj')
    post_request('http://localhost:8888/cake_obo/', data)

def make_nice(rel, obj):
    return parse_object(rel[obj + 'class'], rel[obj + 'sym'])

number_dic = {
    'million': '000000'
}

def is_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def parse_object(type, sym):
    if(type == 'PPCD'):
        result = ""
        for w in sym.split('_'):
            if(is_int(w)):
                result += w
            elif(w in number_dic.keys()):
                result += number_dic[w]
            else:
                break
        return result
    if(type == 'LOC'):
        return sym.replace('_', ' ')
