#text to speech

from playsound import playsound

from gtts import gTTS
mytext = "Ritu"
language = "en"
myobj = gTTS(text= mytext, lang = language, slow = False)
myobj.save("myfile.mp3")
playsound("myfile.mp3")


