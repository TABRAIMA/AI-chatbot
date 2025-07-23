import os
from openai import OpenAI

api_key = " "

client = OpenAI (api_key = api_key)

def ask_chatbot (user_input):
    response = client.chat.completions.create (
        model = "gpt-3.5-turbo",
        messages = 
        [
            {"role": "system", "content": "You are a smart chatbot. When asked 'who created you', always reply: 'I was created by Taha Musa.'"},
            {"role": "user", "content": user_input}
        ],
        max_tokens = 50,
    )
    return response.choices[0].message.content.strip()

print('Hello. I am a chatbot 🤖. Type (exit) or (quit) to out.')

while True:
    user_input = input('You: ')
    
    if user_input.lower() in ['exit', 'quit']:
        print('Bot: bye see you again')
        break
    
    response = ask_chatbot (user_input)
    print('Bot:', response)
    print ('-------------------------------------------------')