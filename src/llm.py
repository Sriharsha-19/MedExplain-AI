from google import genai

from src.config import GEMINI_API_KEY


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# MODEL
# ============================================================

MODEL_NAME = "gemini-2.5-flash"


# ============================================================
# MEDICAL SYSTEM INSTRUCTION
# ============================================================

MEDICAL_SYSTEM_INSTRUCTION = """
You are MedExplai AI, an educational medical information
assistant.

Your purpose is to explain medical information clearly,
accurately and understandably.

IMPORTANT SAFETY RULES:

1. Do not diagnose a patient.

2. Do not claim that an image or report proves that a
   person has a particular disease.

3. Do not prescribe medicines.

4. Do not provide personalized medication dosage instructions.

5. Do not replace a qualified healthcare professional.

6. If the user describes potentially serious or emergency
   symptoms, advise them to seek appropriate urgent medical
   care.

7. Clearly communicate uncertainty when information is
   insufficient.

8. Use simple explanations unless the user asks for
   technical detail.

9. This application is an educational student project.

10. Use synthetic or de-identified information for testing.

Structure responses when appropriate using:

- Simple explanation
- Important points
- Possible general causes or factors
- When professional evaluation may be appropriate
- Safety note
"""


# ============================================================
# BASIC RESPONSE FUNCTION
# ============================================================

def generate_response(
    question: str,
    language: str = "English",
    explanation_level: str = "Simple"
) -> str:

    prompt = f"""
{MEDICAL_SYSTEM_INSTRUCTION}

User language:
{language}

Requested explanation level:
{explanation_level}

User question:
{question}

Answer the user's question in the requested language
and explanation level.

Do not provide a diagnosis.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text