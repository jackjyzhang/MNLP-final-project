import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE """
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate

""" VOLUME """
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

""" VOICE/LANGUAGE """
ch_voice_id = "com.apple.speech.synthesis.voice.ting-ting" # chinese voice id
voices = engine.getProperty('voices')                      # getting details of current voice
#engine.setProperty('voice', voices[0].id)                 # changing index, changes voices. o for male
engine.setProperty('voice', ch_voice_id)

f = open("mtresult.txt", "r")
contents = f.read()
engine.say(contents)
engine.runAndWait()
engine.stop()