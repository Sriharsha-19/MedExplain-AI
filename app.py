import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# =========================================================
# LOAD ENVIRONMENT
# =========================================================

load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found in .env file.")
    st.stop()


# =========================================================
# GROQ CLIENT
# =========================================================

client = Groq(
    api_key=GROQ_API_KEY
)

GROQ_MODEL = "openai/gpt-oss-120b"


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MedExplain AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LANGUAGES
# =========================================================

LANGUAGES = {
    "English": {
        "home": "Home",
        "explainer": "AI Explainer",
        "report": "Report Analyzer",
        "image": "Image Analyzer",
        "chat": "AI Chat",
        "knowledge": "Knowledge Base",
        "language": "Language",
        "welcome": "Welcome to MedExplain AI",
        "welcome_text":
            "Understand medical information in simple language using AI.",
        "quick_access": "Quick Access",
        "new_explanation": "New Explanation",
        "start_chat": "Start Chat",
        "explainer_title": "🧠 AI Medical Explainer",
        "question": "Enter a medical term or question",
        "explain": "Explain",
        "report_title": "📄 Medical Report Analyzer",
        "upload_report": "Upload your medical report",
        "image_title": "🩻 Medical Image Analyzer",
        "upload_image": "Upload a medical image",
        "analyze": "Analyze",
        "chat_title": "💬 AI Medical Chat",
        "chat_placeholder": "Type your medical question...",
        "clear_chat": "Clear Chat",
        "knowledge_title": "📚 Medical Knowledge Base",
        "thinking": "Thinking...",
        "disclaimer":
            "⚠️ MedExplain AI provides educational information only. "
            "It is not a substitute for a qualified medical professional."
    },

    "తెలుగు": {
        "home": "హోమ్",
        "explainer": "AI వివరణ",
        "report": "రిపోర్ట్ విశ్లేషణ",
        "image": "చిత్ర విశ్లేషణ",
        "chat": "AI చాట్",
        "knowledge": "వైద్య జ్ఞానం",
        "language": "భాష",
        "welcome": "MedExplain AI కి స్వాగతం",
        "welcome_text":
            "AI సహాయంతో వైద్య సమాచారాన్ని సులభమైన భాషలో అర్థం చేసుకోండి.",
        "quick_access": "త్వరిత ప్రాప్యత",
        "new_explanation": "కొత్త వివరణ",
        "start_chat": "చాట్ ప్రారంభించండి",
        "explainer_title": "🧠 AI వైద్య వివరణ",
        "question": "వైద్య పదం లేదా ప్రశ్నను నమోదు చేయండి",
        "explain": "వివరించండి",
        "report_title": "📄 వైద్య రిపోర్ట్ విశ్లేషణ",
        "upload_report": "మీ వైద్య రిపోర్ట్‌ను అప్లోడ్ చేయండి",
        "image_title": "🩻 వైద్య చిత్రం విశ్లేషణ",
        "upload_image": "వైద్య చిత్రాన్ని అప్లోడ్ చేయండి",
        "analyze": "విశ్లేషించండి",
        "chat_title": "💬 AI వైద్య చాట్",
        "chat_placeholder": "మీ వైద్య ప్రశ్నను టైప్ చేయండి...",
        "clear_chat": "చాట్ క్లియర్ చేయండి",
        "knowledge_title": "📚 వైద్య జ్ఞాన కేంద్రం",
        "thinking": "ఆలోచిస్తోంది...",
        "disclaimer":
            "⚠️ MedExplain AI విద్యా సమాచారం కోసం మాత్రమే. "
            "ఇది వైద్య నిపుణుడి సలహాకు ప్రత్యామ్నాయం కాదు."
    },

    "हिन्दी": {
        "home": "होम",
        "explainer": "AI व्याख्याता",
        "report": "रिपोर्ट विश्लेषक",
        "image": "इमेज विश्लेषक",
        "chat": "AI चैट",
        "knowledge": "मेडिकल ज्ञान",
        "language": "भाषा",
        "welcome": "MedExplain AI में आपका स्वागत है",
        "welcome_text":
            "AI की सहायता से मेडिकल जानकारी को सरल भाषा में समझें।",
        "quick_access": "त्वरित पहुँच",
        "new_explanation": "नई व्याख्या",
        "start_chat": "चैट शुरू करें",
        "explainer_title": "🧠 AI मेडिकल व्याख्याता",
        "question": "मेडिकल शब्द या प्रश्न दर्ज करें",
        "explain": "समझाएँ",
        "report_title": "📄 मेडिकल रिपोर्ट विश्लेषक",
        "upload_report": "अपनी मेडिकल रिपोर्ट अपलोड करें",
        "image_title": "🩻 मेडिकल इमेज विश्लेषक",
        "upload_image": "मेडिकल इमेज अपलोड करें",
        "analyze": "विश्लेषण करें",
        "chat_title": "💬 AI मेडिकल चैट",
        "chat_placeholder": "अपना मेडिकल प्रश्न टाइप करें...",
        "clear_chat": "चैट साफ करें",
        "knowledge_title": "📚 मेडिकल ज्ञान केंद्र",
        "thinking": "सोच रहा है...",
        "disclaimer":
            "⚠️ MedExplain AI केवल शैक्षणिक जानकारी प्रदान करता है। "
            "यह योग्य चिकित्सा विशेषज्ञ की सलाह का विकल्प नहीं है।"
    }
}


# =========================================================
# SESSION STATE
# =========================================================

if "language" not in st.session_state:
    st.session_state.language = "English"

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

if "explanation" not in st.session_state:
    st.session_state.explanation = ""


L = LANGUAGES[st.session_state.language]


# =========================================================
# LANGUAGE INSTRUCTION
# =========================================================

def language_instruction():

    if st.session_state.language == "తెలుగు":
        return """
Respond completely in Telugu.
Use simple and natural Telugu.
Keep important medical terms in English in brackets when useful.
"""

    if st.session_state.language == "हिन्दी":
        return """
Respond completely in Hindi.
Use simple and natural Hindi.
Keep important medical terms in English in brackets when useful.
"""

    return """
Respond completely in English.
Use simple and easy-to-understand English.
"""


# =========================================================
# MEDICAL SYSTEM INSTRUCTION
# =========================================================

def medical_instruction():

    return f"""
You are MedExplain AI, an educational medical information assistant.

{language_instruction()}

Important rules:

- Provide educational medical information.
- Do not diagnose the user.
- Do not claim to be a doctor.
- Explain medical topics in simple language.
- Explain possible causes and symptoms carefully.
- Symptoms alone cannot confirm a diagnosis.
- Explain general diagnostic methods when relevant.
- Explain general treatment and management information.
- Never tell a user to stop prescribed medication.
- If someone describes a possible emergency, recommend urgent medical care.
- Encourage consultation with a qualified healthcare professional when appropriate.
- Use headings and bullet points for longer answers.
- Be accurate, helpful and easy to understand.
"""


# =========================================================
# GEMINI FUNCTION
# =========================================================

def ask_groq(prompt):

    try:

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": medical_instruction()
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=2048
        )

        if response.choices:
            return response.choices[0].message.content

        return "No response was generated."

    except Exception as e:

        return f"Groq Error: {str(e)}"


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🩺 MedExplain AI")

    st.divider()

    selected_language = st.selectbox(
        L["language"],
        ["English", "తెలుగు", "हिन्दी"],
        index=[
            "English",
            "తెలుగు",
            "हिन्दी"
        ].index(st.session_state.language)
    )

    if selected_language != st.session_state.language:

        st.session_state.language = selected_language

        if selected_language == "English":
            st.session_state.page = "Home"

        elif selected_language == "తెలుగు":
            st.session_state.page = "హోమ్"

        else:
            st.session_state.page = "होम"

        st.rerun()

    st.divider()

    menu = [
        L["home"],
        L["explainer"],
        L["report"],
        L["image"],
        L["chat"],
        L["knowledge"]
    ]

    if st.session_state.page not in menu:
        st.session_state.page = L["home"]

    selected_page = st.radio(
        "Menu",
        menu,
        index=menu.index(st.session_state.page)
    )

    st.session_state.page = selected_page

    st.divider()

    st.subheader(L["quick_access"])

    if st.button(
        "🧠 " + L["new_explanation"],
        use_container_width=True
    ):

        st.session_state.page = L["explainer"]
        st.session_state.explanation = ""
        st.rerun()

    if st.button(
        "💬 " + L["start_chat"],
        use_container_width=True
    ):

        st.session_state.page = L["chat"]
        st.rerun()

    st.divider()

    st.warning(L["disclaimer"])


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    st.title("🩺 MedExplain AI")

    st.header(L["welcome"])

    st.write(L["welcome_text"])

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("🧠 AI Explainer")

        st.write(
            "Ask questions about medical conditions, "
            "symptoms and medical terms."
        )

        if st.button(
            L["explainer"],
            key="home_explainer",
            use_container_width=True
        ):

            st.session_state.page = L["explainer"]
            st.rerun()

    with col2:

        st.subheader("📄 Report Analyzer")

        st.write(
            "Upload a medical report and understand "
            "its information."
        )

        if st.button(
            L["report"],
            key="home_report",
            use_container_width=True
        ):

            st.session_state.page = L["report"]
            st.rerun()

    with col3:

        st.subheader("🩻 Image Analyzer")

        st.write(
            "Upload a medical image for AI-assisted "
            "educational analysis."
        )

        if st.button(
            L["image"],
            key="home_image",
            use_container_width=True
        ):

            st.session_state.page = L["image"]
            st.rerun()

    st.divider()

    col4, col5, col6 = st.columns(3)

    with col4:

        st.subheader("💬 AI Chat")

        st.write(
            "Have a conversation with MedExplain AI "
            "about medical topics."
        )

        if st.button(
            L["chat"],
            key="home_chat",
            use_container_width=True
        ):

            st.session_state.page = L["chat"]
            st.rerun()

    with col5:

        st.subheader("📚 Knowledge Base")

        st.write(
            "Explore common medical topics."
        )

        if st.button(
            L["knowledge"],
            key="home_knowledge",
            use_container_width=True
        ):

            st.session_state.page = L["knowledge"]
            st.rerun()

    with col6:

        st.subheader("🌐 Languages")

        st.write(
            "English • తెలుగు • हिन्दी"
        )

    st.divider()

    st.info(L["disclaimer"])


# =========================================================
# AI EXPLAINER
# =========================================================

def ai_explainer():

    st.title(L["explainer_title"])

    st.write(
        "Ask Gemini to explain a medical topic "
        "in simple language."
    )

    question = st.text_area(
        L["question"],
        placeholder="Example: What is diabetes?",
        height=150
    )

    if st.button(
        "🧠 " + L["explain"],
        type="primary"
    ):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            with st.spinner(L["thinking"]):

                prompt = f"""
Explain the following medical question:

{question}

Structure the response with:

### What does it mean?

### Common symptoms or features

### Common causes

### How is it diagnosed?

### Common treatment or management

### When should someone seek medical help?

### Important things to remember

Do not diagnose the user.
"""

                st.session_state.explanation = ask_groq(
    prompt
)

    if st.session_state.explanation:

        st.divider()

        st.subheader("🤖 Gemini")

        st.markdown(
            st.session_state.explanation
        )


# =========================================================
# REPORT ANALYZER
# =========================================================

def report_analyzer():

    st.title(L["report_title"])

    st.write(
        "Upload a medical report and MedExplain AI will "
        "help you understand the information in simple language."
    )

    uploaded_file = st.file_uploader(
        L["upload_report"],
        type=["pdf", "txt", "docx"],
        key="medical_report"
    )

    if uploaded_file:

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )

        file_name = uploaded_file.name.lower()

        report_text = ""

        # =====================================================
        # PDF
        # =====================================================

        if file_name.endswith(".pdf"):

            try:

                from pypdf import PdfReader

                reader = PdfReader(uploaded_file)

                pages = []

                for page in reader.pages:

                    text = page.extract_text()

                    if text:
                        pages.append(text)

                report_text = "\n\n".join(pages)

            except Exception as e:

                st.error(
                    f"Could not read the PDF: {str(e)}"
                )

        # =====================================================
        # DOCX
        # =====================================================

        elif file_name.endswith(".docx"):

            try:

                from docx import Document

                document = Document(uploaded_file)

                paragraphs = []

                for paragraph in document.paragraphs:

                    if paragraph.text.strip():

                        paragraphs.append(
                            paragraph.text
                        )

                report_text = "\n\n".join(
                    paragraphs
                )

            except Exception as e:

                st.error(
                    f"Could not read the DOCX file: {str(e)}"
                )

        # =====================================================
        # TXT
        # =====================================================

        elif file_name.endswith(".txt"):

            try:

                report_text = uploaded_file.read().decode(
                    "utf-8",
                    errors="ignore"
                )

            except Exception as e:

                st.error(
                    f"Could not read the text file: {str(e)}"
                )

        # =====================================================
        # CHECK REPORT TEXT
        # =====================================================

        if report_text.strip():

            with st.expander(
                "📄 View Extracted Report",
                expanded=False
            ):

                st.text_area(
                    "Extracted Text",
                    report_text,
                    height=300
                )

            st.divider()

            if st.button(
                "🔍 Analyze Report",
                type="primary",
                use_container_width=True
            ):

                with st.spinner(
                    "Analyzing your medical report..."
                ):

                    prompt = f"""
Analyze the following medical report for educational purposes.

IMPORTANT:
- Do not diagnose the patient.
- Do not claim certainty about any disease.
- Do not recommend stopping or changing prescribed medication.
- Explain abnormal values carefully.
- Mention that laboratory reference ranges can vary by laboratory.
- If the report contains an emergency-level finding, clearly recommend contacting a healthcare professional urgently.
- Use simple language.
- Keep important medical terms in English when useful.
- Do not invent information that is not present in the report.

Analyze the report using these sections:

## 1. Report Summary
Give a simple summary of what the report contains.

## 2. Test Results
List the important tests and their reported values.

## 3. What the Results Mean
Explain the results in simple language.

## 4. Results That May Need Attention
Identify values that appear outside the provided reference ranges.

For each one:
- Test name
- Reported value
- Reference range
- Why it may be important

## 5. Results Within the Reported Range
Mention important results that appear within the provided reference ranges.

## 6. What to Discuss With a Doctor
Give useful questions or points the patient can discuss with a qualified healthcare professional.

## 7. Important Note
Clearly state that this is educational information and not a medical diagnosis.

MEDICAL REPORT:

{report_text}
"""

                    result = ask_groq(prompt)

                    st.session_state[
                        "report_analysis"
                    ] = result

            if "report_analysis" in st.session_state:

                st.divider()

                st.subheader(
                    "🤖 MedExplain AI Analysis"
                )

                st.markdown(
                    st.session_state[
                        "report_analysis"
                    ]
                )

        else:

            st.warning(
                "No readable text was found in this file."
            )

            st.info(
                "If this is a scanned PDF, the report may "
                "contain images instead of selectable text. "
                "We can handle scanned reports with the "
                "Image Analyzer/OCR step later."
            )

# =========================================================
# IMAGE ANALYZER
# =========================================================

def image_analyzer():

    st.title(L["image_title"])

    st.write(
        "Upload a medical image and MedExplain AI will "
        "provide educational information about what can "
        "be observed."
    )

    uploaded_image = st.file_uploader(
        L["upload_image"],
        type=["jpg", "jpeg", "png", "webp"],
        key="medical_image"
    )

    if uploaded_image:

        # =====================================================
        # DISPLAY IMAGE
        # =====================================================

        st.success(
            f"Uploaded: {uploaded_image.name}"
        )

        st.image(
            uploaded_image,
            caption=uploaded_image.name,
            use_container_width=True
        )

        st.divider()

        # =====================================================
        # ANALYZE BUTTON
        # =====================================================

        if st.button(
            "🔍 Analyze Medical Image",
            type="primary",
            use_container_width=True
        ):

            with st.spinner(
                "Analyzing medical image..."
            ):

                try:

                    # Read image bytes
                    image_bytes = uploaded_image.getvalue()

                    # Convert image to base64
                    import base64

                    base64_image = base64.b64encode(
                        image_bytes
                    ).decode("utf-8")

                    # Determine image type
                    image_type = uploaded_image.type

                    # =================================================
                    # VISION MODEL
                    # =================================================

                    vision_model = "qwen/qwen3.8-27b"

                    response = client.chat.completions.create(
                        model=vision_model,

                        messages=[
                            {
                                "role": "system",
                                "content": f"""
You are MedExplain AI, an educational medical
information assistant.

{language_instruction()}

IMPORTANT MEDICAL SAFETY RULES:

- This image analysis is for educational purposes only.
- Do not diagnose the patient.
- Do not claim that an image confirms a disease.
- Do not identify a disease with certainty from the image.
- Clearly distinguish observations from possible interpretations.
- Do not invent findings.
- If the image quality is poor, say so.
- Recommend consultation with a qualified healthcare
  professional for proper interpretation.
- If the image appears to show an emergency situation,
  recommend urgent medical evaluation.
- Never tell the user to stop or change prescribed medication.

When discussing the image, explain things in simple language.
"""
                            },
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": """
Analyze this medical image for educational purposes.

Please structure the response as:

## 1. Image Type
Explain what type of medical image this appears to be,
if identifiable.

## 2. General Observations
Describe visible features without making a diagnosis.

## 3. Possible Significance
Explain what the observed features could potentially
represent, while clearly stating that these are not
diagnostic conclusions.

## 4. What Cannot Be Determined
Explain what cannot reliably be determined from this
image alone.

## 5. Questions to Ask a Doctor
Give useful questions that the patient can discuss
with a qualified healthcare professional.

## 6. Important Note
State clearly that AI image analysis is educational
and does not replace interpretation by a qualified
radiologist or healthcare professional.
"""
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url":
                                                f"data:{image_type};base64,{base64_image}"
                                        }
                                    }
                                ]
                            }
                        ],

                        temperature=0.3,
                        max_tokens=2048
                    )

                    # =================================================
                    # GET RESPONSE
                    # =================================================

                    if response.choices:

                        image_result = (
                            response
                            .choices[0]
                            .message
                            .content
                        )

                        st.session_state[
                            "image_analysis"
                        ] = image_result

                    else:

                        st.error(
                            "No analysis was returned."
                        )

                except Exception as e:

                    st.error(
                        f"Image Analysis Error: {str(e)}"
                    )

        # =====================================================
        # SHOW RESULT
        # =====================================================

        if "image_analysis" in st.session_state:

            st.divider()

            st.subheader(
                "🤖 MedExplain AI Analysis"
            )

            st.markdown(
                st.session_state[
                    "image_analysis"
                ]
            )

# =========================================================
# AI CHAT
# =========================================================

def ai_chat():

    st.title(L["chat_title"])

    st.write(
        "Ask Gemini your medical questions."
    )

    for message in st.session_state.chat_messages:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )

    user_message = st.chat_input(
        L["chat_placeholder"]
    )

    if user_message:

        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        with st.chat_message("user"):

            st.markdown(user_message)

        conversation = medical_instruction()

        conversation += """

Continue the conversation with the user.
Answer the latest question clearly.
"""

        for message in st.session_state.chat_messages:

            conversation += (
                f"\n\n{message['role'].upper()}: "
                f"{message['content']}"
            )

        with st.chat_message("assistant"):

            with st.spinner(L["thinking"]):

                answer = ask_groq(
                    conversation
                )

                st.markdown(answer)

        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    st.divider()

    if st.button(
        "🗑️ " + L["clear_chat"]
    ):

        st.session_state.chat_messages = []

        st.rerun()


# =========================================================
# KNOWLEDGE BASE
# =========================================================

def knowledge_base():

    st.title(L["knowledge_title"])

    st.write(
        "Explore common medical topics and learn about "
        "them in simple language."
    )

    # =====================================================
    # TOPIC LIST
    # =====================================================

    topics = {
        "🩸 Diabetes": "Explain diabetes, its types, symptoms, causes, risk factors, diagnosis, treatment, management, and prevention.",

        "❤️ Blood Pressure": "Explain high blood pressure and low blood pressure, their symptoms, causes, risks, diagnosis, treatment, and prevention.",

        "🫁 Respiratory Health": "Explain common respiratory health problems, symptoms, causes, diagnosis, treatment, prevention, and when medical help is needed.",

        "🧠 Brain Health": "Explain general brain health, common neurological problems, warning signs, prevention, and when to seek medical care.",

        "🦴 Bone & Joint Health": "Explain bone and joint health, common problems, symptoms, causes, prevention, and general management.",

        "🍎 Nutrition": "Explain basic nutrition, major nutrients, balanced diet, hydration, healthy eating habits, and common nutrition mistakes.",

        "🧪 Blood Tests": "Explain common blood tests such as CBC, blood glucose, HbA1c, lipid profile, and thyroid tests in simple language.",

        "🫀 Heart Health": "Explain basic heart health, common cardiovascular risk factors, warning signs, prevention, and healthy lifestyle practices."
    }

    # =====================================================
    # SELECT TOPIC
    # =====================================================

    selected_topic = st.selectbox(
        "Select a medical topic",
        list(topics.keys())
    )

    st.divider()

    st.subheader(selected_topic)

    st.write(
        "Learn more about this topic using MedExplain AI."
    )

    # =====================================================
    # GENERATE BUTTON
    # =====================================================

    if st.button(
        "📚 Learn About This Topic",
        type="primary",
        use_container_width=True
    ):

        topic_prompt = f"""
Create an educational explanation about:

{selected_topic}

Cover the following:

## 1. What is it?
Explain the topic in simple language.

## 2. Common Types
Explain important types or categories if applicable.

## 3. Common Symptoms or Features
List the common symptoms or characteristics.

## 4. Causes and Risk Factors
Explain common causes and risk factors.

## 5. How Is It Diagnosed?
Explain common diagnostic methods or tests.

## 6. Treatment and Management
Explain general treatment and management approaches.

## 7. Prevention and Healthy Habits
Explain useful prevention and lifestyle practices.

## 8. When to Seek Medical Help
Explain warning signs that require medical attention.

## 9. Important Things to Remember
Give a short summary.

IMPORTANT:
- This is educational information only.
- Do not diagnose the user.
- Do not claim that the information applies specifically to the user.
- Do not tell anyone to stop or change prescribed medication.
- Use simple language.
- Do not invent medical facts.
"""

        with st.spinner(L["thinking"]):

            knowledge_result = ask_groq(
                topic_prompt
            )

        st.session_state[
            "knowledge_result"
        ] = knowledge_result

        st.session_state[
            "knowledge_topic"
        ] = selected_topic

    # =====================================================
    # SHOW RESULT
    # =====================================================

    if "knowledge_result" in st.session_state:

        st.divider()

        st.subheader(
            "🤖 MedExplain AI"
        )

        st.markdown(
            st.session_state[
                "knowledge_result"
            ]
        )

        st.divider()

        st.info(
            L["disclaimer"]
        )

# =========================================================
# PAGE ROUTING
# =========================================================

if st.session_state.page == L["home"]:

    home_page()

elif st.session_state.page == L["explainer"]:

    ai_explainer()

elif st.session_state.page == L["report"]:

    report_analyzer()

elif st.session_state.page == L["image"]:

    image_analyzer()

elif st.session_state.page == L["chat"]:

    ai_chat()

elif st.session_state.page == L["knowledge"]:

    knowledge_base()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🩺 MedExplain AI • Gemini-powered medical education • "
    + L["disclaimer"]
)