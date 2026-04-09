from dotenv import load_dotenv
from groq import Groq
from os import getenv

load_dotenv()

apiKey = getenv('GROQ_API_KEY')

gClient = Groq(api_key=apiKey)

print("🤖 Type 'exit' to end the session ")
while True: 
    user_input = input('🙋 You: ')
    if user_input.lower() == 'exit':
        break

    response = gClient.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
        {"role": "system", "content": "You are helpful chatbot"},
        {"role": "user", "content": user_input}
        ],
        stream=True
    )
    
    print("🤖 Bot: ", end="")
    for chunk in response:
        print(chunk.choices[0].delta.content or "", end="", flush=True)
    print('\n')
