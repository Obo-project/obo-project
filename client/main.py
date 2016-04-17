import server

import re
import rel_extract_obo

dic = {
	"people": "PPUNIT",
	"inhabitants": "PPUNIT"
}

def f(a , b):
	if a in dic:
		return dic[a]
	else:
		return b

sents = "Paris in Berlin and in Brazil in Paris in Moscow."
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

print(sents)

IN = re.compile(r'.*\bin\b(?!\b.+ing)')

class doc():
    pass

doc.headline = ['foo']
doc.text = sents

for rel in extract_rels('LOC', 'LOC', doc, corpus='ieer', pattern=IN):
	print(nltk.sem.relextract.rtuple(rel))
