from server import post_request
import speech_recognition as sr

import nltk
import re
from rel_extract_obo import precompute, extract_rels
from relations.hasPopulation import *

def callback(recognizer, audio):
	try:
		sents = recognizer.recognize_google(audio , language = "en")
		print(sents)
		sents = precompute(sents)
		relations = hasPopulation.extract(sents)
		for rel in relations:
		    rel.post();

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError:
		print("Could not request results from Google Speech Recognition service")

r = sr.Recognizer()
m = sr.Microphone()
#m.SAMPLE_RATE = 48000
with m as source:
	r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
import time
for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
for i in range(10**4):
	print() # calling this function requests that the background listener stop listening
	time.sleep(1)
while True: time.sleep(0.1)
