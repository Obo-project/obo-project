from server import post_request
import speech_recognition as sr

import nltk
import re
from rel_extract_obo import precompute, extract_rels

LIVE_IN = re.compile(r'.*(live|lives|inhabit|inhabits|are|is).*\bin\b(?!\b.+ing)')
THERE = re.compile(r'.*(There are|there are|There is|there is)')
IN = re.compile(r'\bin\b')

def callback(recognizer, audio):
	try:
		sents = recognizer.recognize_google(audio , language = "en")
		print(sents)
		sents = precompute(sents)

		for rel in extract_rels('PPCD', 'LOC', sents, patterns={'left': None, 'middle': LIVE_IN}):
			print(nltk.sem.relextract.rtuple(rel))
			post_request('http://localhost:8888/cake_obo/', "entity=France&relation=population&quantity=65000000")

		for rel in extract_rels('PPCD', 'LOC', sents, patterns={'left': THERE, 'middle': IN}):
			print(nltk.sem.relextract.rtuple(rel))



	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError:
		print("Could not request results from Google Speech Recognition service")

r = sr.Recognizer()
m = sr.Microphone()
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
