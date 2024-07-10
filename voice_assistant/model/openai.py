import os
import openai
open.api_key = ''
messages = [{"role": "system", "content": "You are intelligent assistant."}]
def info():
    message = audio().replace(" ","")

    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion,create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message

    print("Chatgpt:", reply.content)
    speak(reply.content)
    messages.append(reply)