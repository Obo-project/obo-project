import server

import nltk
import re
from rel_extract_obo import extract_rels

dic = {
	"people": "PPUNIT",
	"inhabitants": "PPUNIT"
}

def f(a , b):
	if a in dic:
		return dic[a]
	else:
		return b

sents = "There are 6000000 million people in France."
print(sents)

sents = nltk.sent_tokenize(sents)
sents = [nltk.word_tokenize(sent) for sent in sents]
sents = [nltk.pos_tag(sent) for sent in sents]
sents = [[(a, f(a, b)) for (a,b) in sent] for sent in sents]
sents = nltk.ne_chunk(sents[0])

grammar = """
	CDD: {<CD>*}
	PPCD: {<CDD><PPUNIT>}
	LOC: {<GPE>}
	"""

cp = nltk.RegexpParser(grammar, loop = 2)
sents = cp.parse(sents)

LIVE_IN = re.compile(r'.*(live|lives|inhabit\inhabits).*\bin\b(?!\b.+ing)')

for rel in extract_rels('PPCD', 'LOC', sents, corpus='ieer', pattern=LIVE_IN):
	print(nltk.sem.relextract.rtuple(rel))
