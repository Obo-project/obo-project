from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, treebank
from nltk.stem import WordNetLemmatizer
from nltk.tag import tnt
from nltk.chunk import ne_chunk

from taggers import NamesTagger
import pickle


def tokenize(text):
	"""Tokenize a text"""
	sents = sent_tokenize(text)
	sents = [ word_tokenize(sent) for sent in sents]

	return sents

def simplify(words):
	"""Take a sentence and removes senseless words"""

	english_stopwords = set(stopwords.words('english'))
	words = [word for word in words if word not in english_stopwords]

	return words

def lemmatize(words):
	"""Replace words with lemmas"""
	lemmatizer = WordNetLemmatizer()
	words = [ lemmatizer.lemmatize(word) for word in words]

	return words

def trainPosTagger():
	train_sents = treebank.tagged_sents()[:3000]
	test_sents = treebank.tagged_sents()[3000:]

	name_tagger = NamesTagger()
	tnt_tagger = tnt.TnT(unk=name_tagger , Trained=True)
	tnt_tagger.train(train_sents)
	print(tnt_tagger.evaluate(test_sents))

	f = open('tagger.pickle' , 'wb')
	pickle.dump(tnt_tagger , f)
	f.close()

def loadPosTagger():
	f = open('tagger.pickle' , 'rb')

	tagger = pickle.load(f)
	f.close()

	return tagger


def POS_tagging(words , tagger):
	"""Does the POS tagging using tnt"""


	return tagger.tag(words)

def NE(words):
	"""Recognizes named entities"""

	return ne_chunk(words)

#trainPosTagger()
tagger = loadPosTagger()

sents = tokenize("Barack Obama is the first black president of the United States of America")
sentence = sents[0]
sentence = simplify(sentence)
sentence = lemmatize(sentence)
sentence = POS_tagging(sentence, tagger)
print(sentence)
sentence = NE(sentence)
print(sentence)