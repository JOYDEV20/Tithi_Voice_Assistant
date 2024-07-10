import datetime
import wikipedia
import requests
from gpiozero import CPUTemperature
import openai
import pyautogui
import psutil
import signal
import os
import time 

class VoiceAssistantModel:
    
    def get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M %p")

    def get_current_date(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")
    def wiki(self,query):
        try:
            results = wikipedia.summary(query, sentences=2)
            return results
        except wikipedia.DisambiguationError as e:
            return f"Your query may refer to multiple things. Please be more specific: {e.options}"
        except wikipedia.PageError:
            return "Sorry, I could not find any information on that topic."



    def get_weather(self,city):
        api_key = "8d787e18012752a67660b3d517681ff0"  # Replace with your actual OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather = data["weather"][0]
            description = weather["description"]
            temp = main["temp"]
            return f"The weather in {city} is currently {description} with a temperature of {temp}°C."
        else:
            return "Sorry, I couldn't fetch the weather information. Please check the city name and try again."

    def get_CPUTemp(self):
        cpu = CPUTemperature()
        print(cpu)
    
    def close_window(self, process_name):
        pyautogui.hotkey('alt' + 'f4')
        time.sleep(2)

        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                pid = proc.info['pid']
                os.kill(pid, signal.SIGTERM)
                print("process close")