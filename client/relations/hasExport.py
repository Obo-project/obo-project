from relation import relation, relationData
import re

UNIVERSAL = re.compile(r'.*')

IS_EXPORT = re.compile(r'.*export.*is.*')
S_IS_EXPORT = re.compile(r'.*\'s.*export.*is.*')
IS_EXPORT_MORE = re.compile(r'.*export.*is.*(greater|exceed)')
S_IS_EXPORT_MORE = re.compile(r'.*\'s.*export.*is.*(greater|exceed)')
IS_EXPORT_LESS = re.compile(r'.*export.*is.*(shorter|below)')
S_IS_EXPORT_LESS = re.compile(r'.*\'s.*export.*is.*(shorter|below)')

S_ACCOUNTED_FOR_EXPORT = re.compile(r'.*\'s.*export.*accounted.*for.*')
ACCOUNTED_FOR_EXPORT = re.compile(r'.*export.*account.*for.*')
S_ACCOUNTED_FOR_EXPORT_MORE = re.compile(r'.*\'s.*export.*accounted.*for.*(more.*than)')
ACCOUNTED_FOR_EXPORT_MORE = re.compile(r'.*export.*account.*for.*(more.*than)')
S_ACCOUNTED_FOR_EXPORT_LESS = re.compile(r'.*\'s.*export.*accounted.*for.*(less.*than)')
ACCOUNTED_FOR_EXPORT_LESS = re.compile(r'.*export.*account.*for.*(less.*than)')

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

hasExport = relation('hasExport' , 'GPE' , 'CDD' , make_nice , patterns_list=[
    {'left': UNIVERSAL, 'middle': IS_EXPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_IS_EXPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_EXPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_EXPORT_MORE, 'comparator': 'more', 'inverted': True},
    {'left': UNIVERSAL, 'middle': IS_EXPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_IS_EXPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_EXPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_EXPORT_LESS, 'comparator': 'less', 'inverted': True},
    {'left': UNIVERSAL, 'middle': IS_EXPORT, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_IS_EXPORT, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': ACCOUNTED_FOR_EXPORT, 'comparator': 'egal', 'inverted': True},
    {'left': UNIVERSAL, 'middle': S_ACCOUNTED_FOR_EXPORT, 'comparator': 'egal', 'inverted': True}
])
