import re

import speech_recognition as sr
import nltk

from server import post_request
from precompute import precompute
from supportedRelations import *
from supportedRelations import listeRelation

def callback(recognizer, audio):
	try:
		sents = recognizer.recognize_google(audio , language = "en")
		print(sents)
		sents = precompute(sents)
		print(sents)
		for relation in listeRelation:
		    rels = relation.extract(sents)

		    for rel in rels:
		        rel.post();

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError:
		print("Could not request results from Google Speech Recognition service")

#SAMPLE_RATE = 44000;
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
	r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

import time
while True: time.sleep(0.1)
