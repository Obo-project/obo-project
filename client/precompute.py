import nltk

from supportedRelations import dic, grammar

def precompute(sents):

    def f(a , b):
    	if a in dic:
    		return dic[a]
    	else:
    		return b

    def g(a):
        if a == 'GDP':
            return 'gdp'
        else:
            return a

    sents = nltk.sent_tokenize(sents)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    sents = [[(g(a), f(a, b)) for (a,b) in sent] for sent in sents]
    sents = nltk.ne_chunk(sents[0])

    cp = nltk.RegexpParser("\n".join(grammar), loop = 5)
    sents = cp.parse(sents)
    print("\n".join(grammar))
    return sents
