import re
from rel_extract_obo import extract_rels
from server import post_request

number_dic = {
    'million': '000000'
}

class relation(object):

    def __init__(self, relationName , subjclass , objclass , patterns):

        self.relationName = relationName
        self.objclass = objclass
        self.subjclass = subjclass

        self.patterns = patterns

    def extract(self, sentence):

        relations = extract_rels(self.subjclass , self.objclass , sentence , patterns=self.patterns)

        return [relationData(self, rel) for rel in relations]

def replace_int(x):
    if (type(x) != int and x in number_dic.keys()):
        return number_dic[x]
    else:
        return x

def make_nice(text):
    text = [replace_int(x) for x in text.split('_')]
    return " ".join(text)

class relationData(object):

    def __init__(self, relation, rel):

        self.objet = make_nice(rel['objsym'])
        self.subject = make_nice(rel['subjsym'])
        self.relation = relation

    def post(self):
        data = {'entity':self.relation.relationName , 'object':self.objet , 'subject':self.subject}
        post_request('http://localhost:8888/cake_obo/', data)
