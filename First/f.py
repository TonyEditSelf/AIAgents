from dotenv import load_dotenv
from os import getenv

load_dotenv()

apiKey = getenv('OPENAI_API_KEY')

print(apiKey)