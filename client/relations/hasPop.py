from relation import relation, relationData
import re

THERE = re.compile(r'.*((There.*are)|(there.*are)|(There.*is)|(there.*is))')
IN = re.compile(r'\bin\b')

number_dic = {
    'million': '000000'
}

def replace_int(x):
    if (type(x) != int and x in number_dic.keys()):
        return number_dic[x]
    else:
        return x

def make_nice(text):
    text = [replace_int(x) for x in text.split('_')]
    return " ".join(text)

hasPop = relation('hasPopulation' , 'PPCD' , 'LOC' , make_nice , patterns={'left':THERE, 'middle': IN})
