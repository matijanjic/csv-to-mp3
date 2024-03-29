from gtts import gTTS
import os

os.chdir('/home/matija/Desktop/TTS')

with open("sentences.csv", "r") as t:
    contents = t.read()
    split = contents.split('\n')


language = "en"

index = 1

for article in split:
    
    if article.strip():
        myobj = gTTS(text = article, lang = language, slow = False)
        myobj.save("output/pairs/%s.mp3" % article)
        index += 1

