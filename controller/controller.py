from model.voice_assistant_model import VoiceAssistantModel
import os
from pynput import keyboard
import webbrowser
import keyboard
import time
from model.listen import listen_audio
from view.voice_assistant_view import VoiceAssistantView 
from model.tts import TextToSpeech
from model.contact.contact import save_contact, get_contact
# speak = TextToSpeech.py_pyttsx3()

class VoiceAssistantController:
    def __init__(self):
        self.model = VoiceAssistantModel()
        self.view = VoiceAssistantView()
        self.listen = listen_audio()
        self.tts = TextToSpeech()
    def run(self):
        speak = self.tts.py_pyttsx3    
        while True:
            # speak("Hello i'm a virtual assistant")
            query = self.listen.get_audio().lower()
            
            if 'hello tithi' in query or 'wake up tithi' in query:
                speak("Hello Joy, how may i assist you")
                while True:
                    query = self.listen.get_audio().lower()
                    if 'time' in query:
                        current_time = self.model.get_current_time()
                        self.view.show_time(current_time)
                        speak("Now the time is" + current_time)
                    elif 'thank you' in query:
                        speak("have a good day, call me again joy")
                        break
                    elif 'wikipedia' in query:
                        speak("Searching Wikipedia .......")
                        query = query.replace('wikipedia', '')
                        results = self.model.wiki(query)
                        print(results)
                        speak(results)
                    elif 'weather' in query:         
                         speak("Please tell me the city name.")
                         city = self.listen.get_audio().lower()
                         if city:
                            speak("Fetching weather information...")
                            weather_report = self.model.get_weather(city)
                            speak(weather_report)
                         else:
                            speak("Please say a command with 'Wikipedia' to search for information or 'weather' to get the weather report.")
                    
                    elif 'convert currency' in query:
                        speak("Please tell me the amount and the currencies to convert from and to.")
                        amount = float(self.listen.get_audio().lower())
                        from_currency = self.listen.get_audio().lower()
                        to_currency = self.listen.get_audio().lower()
                        conversion_result = self.model.convert_currency(amount, from_currency, to_currency, "91ea426cc5c37563e81c99a1c6")
                        speak(conversion_result)

                    elif 'save contact' in query:
                        speak("Please tell me the name.")
                        name = self.listen.get_audio().lower()
                        speak(f"Please tell me the number for {name}.")
                        number = self.listen.get_audio().lower()
                        confirmation = save_contact(name, number)
                        speak(confirmation)
                    elif 'show contact' in query:
                        speak("Please tell me the name.")
                        name = self.listen.get_audio().lower()
                        contact_number = get_contact(name)
                        speak(contact_number)
                    elif 'Temperature' in query:
                        Temp= self.model.get_CPUTemp()
                        print(Temp)
                        speak( "Now my temperature is" + Temp)
                    elif "search" in query:
                        speak("What do you want to search")
                        
                    elif "light on" in query:

                        webbrowser.open("https://blr1.blynk.cloud/external/api/update?token=1T-W2mLOA2FwYz4RmR8LWKkYswo7i4lx&v0=1")
                       
                        time.sleep(0.5)
                        self.model.close_window(process_name= 'chromium-browser')
                        speak("turn on the light")
                    elif "light off" in query:
                        webbrowser.open("https://blr1.blynk.cloud/external/api/update?token=1T-W2mLOA2FwYz4RmR8LWKkYswo7i4lx&v0=0")
                        time.sleep(0.5)
                        self.model.close_window(process_name= 'chromium-browser')
                        speak("turn off the light")
                    elif "bye" in query:
                        speak("Have a nice day. call me again")
                        break