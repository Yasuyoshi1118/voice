from gtts import gTTS #pip install gTTs
import subprocess
import os
import time

mytext = "登録のないレンジです。　注意してください"

language = "ja"

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("ng.mp3")

#subprocess.call("aplay London.mp3", shell=True)
os.system("start ng.mp3")
