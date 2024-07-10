import pyaudio
import pyttsx3
import nltk
from gtts import gTTS
import os
class TextToSpeech:
    def py_pyttsx3(self, text):
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init('espeak')
        
        voices = engine.getProperty('voices')
        # Set properties (optional)
        engine.setProperty('voice', 'english_rp+f3')
        engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)


        # Speak the text
        engine.say(text)

        # Wait for speech to finish
        engine.runAndWait()



















    # def py_gtts(self, text):
    #     tts=gTTS(text=text, lang='en')

    #     tts.save("./model/sound/temp.mp3")

    #     os.system("temp.mp3")

    #     os.remove("temp.mp3")
    # def speak(self, text, use_gtts=False):
    #     if use_gtts:
    #         self.py_gtts(text)
    #     else:
    #         self.py_pyttsx3(text)
# tts = TextToSpeech()
# tts.py_pyttsx3("Hello")