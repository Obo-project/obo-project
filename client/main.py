import server

import nltk
import re
from rel_extract_obo import precompute, extract_rels

sents = "60 million people live in France"
print(sents)
sents = precompute(sents)

LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is).*\bin\b(?!\b.+ing)')

for rel in extract_rels('PPCD', 'LOC', sents, pattern=LIVE_IN):
	print(nltk.sem.relextract.rtuple(rel))
