# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("Hello, I am a text to speech engine. I can convert text to speech. I can speak any text you want me to speak. I can also speak in different languages. I can also speak in different voices. I can also speak in different rates. I can also speak in different volumes. I can also speak in different pitches. I can also speak in different tones. I can also speak in different accents. I can also speak in different styles. I can also speak in different emotions. I can also speak in different moods. I can also speak in different personalities. I can also speak in different characters. I can also speak in different languages and accents. I can also speak in different voices and styles. I can also speak in different rates and volumes. I can also speak in different pitches and tones. I can also speak in different emotions and moods. I can also speak in different personalities and characters.")
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()