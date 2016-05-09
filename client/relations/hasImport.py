from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
IS_IMPORT = re.compile(r'.*import\bis\b.*')
S_IMPORT = re.comple(r'.*\'s\bimport.*is.*')
S_ACCOUNTED_FOR = re.compile(r'.*\'s\bimport.*\baccounted\b.*for.*')
ACCOUNTED_FOR = re.compile(r'.*import.*accounted\b.*for.*')


def make_nice(x):
    return x

hasImport = relation('hasImport' , 'GPE' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': IS, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': S_IS, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR, 'comparator': 'egal'},
])
