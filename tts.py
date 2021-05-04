from gtts import gTTS
import os

os.chdir('/home/matija/Desktop/TTS')

with open("test.txt", "r") as t:
    contents = t.read()
    split = contents.split('\n\n')


language = "en"

index = 1

for article in split:
    
    if article.strip():
        myobj = gTTS(text = article, lang = language, slow = False)
        myobj.save("text%s.mp3" % index)
        index += 1

