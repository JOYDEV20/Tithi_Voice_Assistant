import pyaudio
import os
import sys
import speech_recognition as sr

class listen_audio:
    def get_audio(self):
        r = sr.Recognizer()
        print(sr.Microphone.list_microphone_names())
        with sr.Microphone() as source:
            print("Listening......")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)       
            said = ""

            try:
                print("Recognizing......")
                said = r.recognize_google(audio, language="en-US")
                print(said)
            except Exception as e:
                print("Exception: " + str(e))

        return said
    # while True:
    #     query = get_audio().lower()
    #     if 'Hello' in query:
    #         print("Hi joy. How may i assist you")

   