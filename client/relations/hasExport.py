from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')
IS_EXPORT = re.compile(r'.*export\bis\b.*')
S_IS_EXPORT = re.comple(r'.*\'s\bimport.*is.*')
S_ACCOUNTED_FOR_EXPORT = re.compile(r'.*\'s\bexport.*\baccounted\b.*for.*')
ACCOUNTED_FOR_EXPORT = re.compile(r'.*export.*accounted\b.*for.*')


def make_nice(x):
    return x

hasImport = relation('hasImport' , 'GPE' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': IS_EXPORT, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': S_IS_EXPORT, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_EXPORT, 'comparator': 'egal'},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_EXPORT, 'comparator': 'egal'},
])
