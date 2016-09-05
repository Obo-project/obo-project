import re

from relation import relation, relationData
from supportedRelations import listeRelation

UNIVERSAL = re.compile(r'.*')

IS_IMPORT = re.compile(r'.*import.*is.*')
S_IS_IMPORT = re.compile(r'.*\'s.*import.*is.*')
IS_IMPORT_MORE = re.compile(r'.*import.*is.*(greater|exceed|above)')
S_IS_IMPORT_MORE = re.compile(r'.*\'s.*import.*is.*(greater|exceed|above)')
IS_IMPORT_LESS = re.compile(r'.*import.*is.*(shorter|below|lower|under)')
S_IS_IMPORT_LESS = re.compile(r'.*\'s.*import.*is.*(shorter|below|lower|under)')

S_ACCOUNTED_FOR_IMPORT = re.compile(r'.*\'s.*import.*accounted.*for.*')
ACCOUNTED_FOR_IMPORT = re.compile(r'.*import.*account.*for.*')
S_ACCOUNTED_FOR_IMPORT_MORE = re.compile(r'.*\'s.*import.*accounted.*for.*(more.*than)')
ACCOUNTED_FOR_IMPORT_MORE = re.compile(r'.*import.*account.*for.*(more.*than)')
S_ACCOUNTED_FOR_IMPORT_LESS = re.compile(r'.*\'s.*import.*accounted.*for.*(less.*than)')
ACCOUNTED_FOR_IMPORT_LESS = re.compile(r'.*import.*account.*for.*(less.*than)')

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

def make_nice(timt):
    timt = [replace_int(x) for x in timt.split('_')]
    return("".join(timt))

hasImport = relation('hasImport' , 'GPE' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': IS_IMPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_IS_IMPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_IMPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_IMPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': IS_IMPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_IS_IMPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_IMPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_IMPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': IS_IMPORT, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_IS_IMPORT, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_IMPORT, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_IMPORT, 'comparator': 'egal', 'inverted': True}
])

listeRelation.append(hasImport)
