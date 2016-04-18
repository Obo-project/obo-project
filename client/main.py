import server

import nltk
import re
from rel_extract_obo import precompute, extract_rels

sents = "There are 60000000 million people in France"
print(sents)
sents = precompute(sents)

LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is).*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*(There are|There is)')
IN = re.compile(r'\bin\b')

for rel in extract_rels('PPCD', 'LOC', sents, patterns={'left': None, 'middle': LIVE_IN}):
	print(nltk.sem.relextract.rtuple(rel))

for rel in extract_rels('PPCD', 'LOC', sents, patterns={'left': THERE, 'middle': IN}):
	print(nltk.sem.relextract.rtuple(rel))
