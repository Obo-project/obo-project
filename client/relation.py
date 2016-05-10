import re
from relextract import extract_rels
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
            relations += extract_rels(self.subjclass , self.objclass , sentence , patterns=patterns)
            if relations != []:
                break
        return [relationData(self, rel, self.make_nice, comparator=rel['comparator'], inverted=rel['inverted']) for rel in relations]

class relationData(object):
    def __init__(self, relation, rel, make_nice, comparator='egal', inverted=False):
        self.object = rel['objsym']
        self.subject = rel['subjsym']
        self.relation = relation
        self.comparator = comparator
        self.inverted = inverted
        self.make_nice = make_nice

    def post(self):
        if(self.inverted):
            data = {'relation':self.relation.relationName, 'object':" ".join([x for x in self.subject.split('_')]), 'subject': self.make_nice(self.object), 'comparator':self.comparator}
        else:
            data = {'relation':self.relation.relationName, 'object':" ".join([x for x in self.object.split('_')]), 'subject': self.make_nice(self.subject), 'comparator':self.comparator}

        post_request('http://localhost:8888/cake_obo/', data)
