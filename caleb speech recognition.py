>>> import speech recognition as sr
>>>sr._version_
'3.9.0'

>>> r = sr.Recognizer()

>>> r.recognize_google()

>>> caleb = sr.AudioFile('caleb.wav')
>>> with caleb as source
... audio = r.record(source)
...
>>> type(audio)
<class 'speech_recognition.AudioData'>
>>> r.recognze_google(audio)
