import re
from rel_extract_obo import extract_rels
from server import post_request

class relation(object):

    def __init__(self, relationName , subjclass , objclass , make_nice, patterns):

        self.relationName = relationName
        self.objclass = objclass
        self.subjclass = subjclass
        self.make_nice = make_nice

        self.patterns = patterns

    def extract(self, sentence):

        relations = extract_rels(self.subjclass , self.objclass , sentence , patterns=self.patterns)

        return [relationData(self, rel, self.make_nice) for rel in relations]

class relationData(object):

    def __init__(self, relation, rel, make_nice):

        self.objet = make_nice(rel['objsym'])
        self.subject = make_nice(rel['subjsym'])
        self.relation = relation

    def post(self):
        data = {'entity':self.relation.relationName , 'object':self.objet , 'subject':self.subject}
        post_request('http://localhost:8888/cake_obo/', data)
