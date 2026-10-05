import os
from dotenv import load_dotenv

load_dotenv(override=True)

key = os.getenv("GROQ_API_KEY")

if not key:
    print("❌ GROQ_API_KEY was NOT found")
else:
    print("✅ GROQ_API_KEY was found")
    print("Key starts with:", key[:8])
    print("Key length:", len(key))