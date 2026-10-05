import os
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Application settings
APP_NAME = "MedExplai AI"

APP_VERSION = "1.0"

DEFAULT_LANGUAGE = "English"

DEFAULT_EXPLANATION_LEVEL = "Simple"


# Validate API key
if not GEMINI_API_KEY:

    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please add GEMINI_API_KEY to your .env file."
    )