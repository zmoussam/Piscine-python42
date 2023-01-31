#pip install gTTs
from gtts import gTTS

#data 
txt = "welcome in my channel zakaria"
langue = 'en'

#pass data as parameter
res = gTTS(text=txt, lang=langue)
res.save("audio.mp3")