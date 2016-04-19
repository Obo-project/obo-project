import re
from rel_extract_obo import extract_rels
from server import post_request

class relation(object):

    def __init__(self, relationName , subjclass , objclass , make_nice, patterns_list):
        self.relationName = relationName
        self.objclass = objclass
        self.subjclass = subjclass
        self.make_nice = make_nice
        self.patterns_list = patterns_list

    def extract(self, sentence):
        relations = []
        for patterns in self.patterns_list:
            #print(patterns)
            #print(extract_rels(self.subjclass , self.objclass , sentence , patterns=patterns))
            relations += extract_rels(self.subjclass , self.objclass , sentence , patterns=patterns)
        return [relationData(self, rel, self.make_nice, comparator=rel['comparator']) for rel in relations]

class relationData(object):

    def __init__(self, relation, rel, make_nice, comparator='egal'):
        self.objet = rel['objsym']
        self.subject = make_nice(rel['subjsym'])
        self.relation = relation
        self.comparator = comparator

    def post(self):
        data = {'relation':self.relation.relationName, 'entity':self.objet, 'quantity':self.subject, 'comparator':self.comparator}
        post_request('http://localhost:8888/cake_obo/', data)
