import server
import re
import nltk

from rel_extract_obo import precompute, extract_rels

sents = "60 million people live in France"
sents = precompute(sents)

IN = re.compile(r'.*\bin\b(?!\b.+ing)')

for rel in extract_rels('PPCD', 'LOC', sents, pattern=IN):
	print(nltk.sem.relextract.rtuple(rel))
