from nltk.chunk import ChunkParserI
from nltk.chunk.util import conlltags2tree
from nltk.corpus import gazetteers
from nltk.corpus import names

class LocationChunker(ChunkParserI):

	def __init__(self):
		self.locations = set(gazetteers.words())
		self.lookahead = 0

		for loc in self.locations:
			nwords = loc.count(' ')

			if nwords > self.lookahead :
				self.lookahead = nwords

	def iob_locations(self, tagged_sent):
		
		i = 0
		l = len(tagged_sent)
		
		inside = False
		
		while i < l:
			
			word, tag = tagged_sent[i]
			j = i + 1
			k = j + self.lookahead
			nextwords, nexttags = [], []
			loc = False
			
			while j < k:
				if ' '.join([word] + nextwords) in self.locations:
					if inside:
						yield word, tag, 'I-LOCATION'
					else:
						yield word, tag, 'B-LOCATION'
			
					for nword, ntag in zip(nextwords, nexttags):
						yield nword, ntag, 'I-LOCATION'
			
					loc, inside = True, True
					i = j
					break
			
				if j < l:
					nextword, nexttag = tagged_sent[j]
					nextwords.append(nextword)
					nexttags.append(nexttag)
					j += 1
				else:
					break
				
			if not loc:
				inside = False
				i += 1
				yield word, tag, 'O'


	def parse(self, tagged_sent):
	
		iobs = self.iob_locations(tagged_sent)
		return conlltags2tree(iobs)

class PersonChunker(ChunkParserI):
	def __init__(self):
		self.name_set = set(names.words())

	def parse(self, tagged_sent):
		iobs = []
		in_person = False

		for word, tag in tagged_sent:

			if word in self.name_set and in_person:
				iobs.append((word, tag, 'I-PERSON'))

			elif word in self.name_set:
				iobs.append((word, tag, 'B-PERSON'))
				in_person = True
				
			else:
				iobs.append((word, tag, 'O'))
				in_person = False
		
		return conlltags2tree(iobs)