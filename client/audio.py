#!/usr/bin/env python3
import pyaudio
import wave

def play(son):
    chunk = 1024
    p = pyaudio.PyAudio()
    wf = wave.open(son, 'rb')
    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)
    data = wf.readframes(chunk)

    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()
