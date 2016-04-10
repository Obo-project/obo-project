from nltk.tag import SequentialBackoffTagger
from nltk.corpus import names

class NamesTagger(SequentialBackoffTagger):

	def __init__(self, *args, **kwargs):
		SequentialBackoffTagger.__init__(self, *args, **kwargs)
		self.names_set = set([n.lower() for n in names.words()])

	def choose_tag(self, tokens, index, history):
		word = tokens[index]

		if word.lower() in self.names_set:
			return 'NNP'
		else:
			return 'NN'
