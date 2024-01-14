# config/settings.py

import os

from dotenv import load_dotenv

load_dotenv()

CUSTOM_API_KEY = os.getenv("CUSTOM_API_KEY", "")
