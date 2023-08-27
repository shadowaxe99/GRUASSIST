
# settings.py

import os
from dotenv import load_dotenv

load_dotenv()

# Gmail API settings
GMAIL_API_CREDENTIALS = os.getenv('GMAIL_API_CREDENTIALS')

# ChatGPT settings
CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')


