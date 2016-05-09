from relations import dic, grammar
import nltk

def precompute(sents):

    def f(a , b):
    	if a in dic:
    		return dic[a]
    	else:
    		return b

    sents = nltk.sent_tokenize(sents)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    sents = [[(a, f(a, b)) for (a,b) in sent] for sent in sents]
    sents = nltk.ne_chunk(sents[0])

    cp = nltk.RegexpParser(grammar, loop = 5)
    sents = cp.parse(sents)

    return sents
