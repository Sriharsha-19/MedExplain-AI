# 🩺 MedExplain AI

MedExplain AI is an AI-powered medical education application built with **Streamlit** and **Groq**.

It helps users understand medical information in simple language through AI explanations, medical report analysis, image analysis, conversational chat, and a medical knowledge base.

> ⚠️ **Medical Disclaimer:** MedExplain AI is intended for educational and informational purposes only. It does not provide medical diagnoses or replace advice from a qualified healthcare professional.

---
![MedExplain_AI](https://github.com/Sriharsha-19/MedExplain-AI/blob/6095743f41eac5e9e722902e4de25e24236d84b8/Interface.png)

## ✨ Features

### 🧠 AI Medical Explainer

Ask questions about medical terms, conditions, symptoms, tests, and treatments.

The AI provides explanations in simple language.
![MedExplain_AI](https://github.com/Sriharsha-19/MedExplain-AI/blob/6c9188b6cf0b5c7287944232ac5acdaa0ef23357/AI-Explainer.png)

### 📄 Medical Report Analyzer

Upload:

* PDF
* DOCX
* TXT

The application extracts the report text and provides an educational analysis including:

* Report summary
* Test results
* Explanation of results
* Results that may need attention
* Results within the reported range
* Questions to discuss with a doctor

### 🩻 Medical Image Analyzer

Upload medical images such as:

* JPG
* JPEG
* PNG
* WEBP

The AI provides educational observations about the uploaded image.

Image analysis should not be considered a medical diagnosis.

### 💬 AI Medical Chat

Have a conversation with MedExplain AI about medical topics.

The application maintains the conversation during the session.

### 📚 Medical Knowledge Base

Explore common medical topics such as:

* Diabetes
* Blood Pressure
* Respiratory Health
* Brain Health
* Bone & Joint Health
* Nutrition
* Blood Tests
* Heart Health

### 🌐 Multilingual Support

The application supports:

* 🇬🇧 English
* 🇮🇳 తెలుగు (Telugu)
* 🇮🇳 हिन्दी (Hindi)

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Groq API**
* **Groq AI Models**
* **PyPDF**
* **python-docx**
* **python-dotenv**

---

## 📁 Project Structure

```text
MedExplain_Ai/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

**Never publish your API key on GitHub or share it publicly.**

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 🧭 Application Navigation

The application contains the following sections:

```text
🩺 MedExplain AI
│
├── 🏠 Home
├── 🧠 AI Explainer
├── 📄 Report Analyzer
├── 🩻 Image Analyzer
├── 💬 AI Chat
└── 📚 Knowledge Base
```

---

## 🔐 Security

API credentials are stored in environment variables rather than directly inside the Python source code.

The `.env` file should never be committed to a public Git repository.

The project uses `.gitignore` to prevent accidental exposure of environment files.

---

## ⚠️ Medical Safety

MedExplain AI is an educational AI application.

It should **not** be used to:

* Diagnose diseases
* Replace a doctor
* Replace a radiologist
* Decide whether to start or stop medication
* Replace emergency medical care

Users should consult qualified healthcare professionals for diagnosis, treatment, and interpretation of medical reports or images.

If someone is experiencing symptoms that may indicate an emergency, they should seek urgent medical attention.

---

## 🚀 Future Improvements

Possible future improvements include:

* OCR for scanned medical reports
* Improved medical image analysis
* More medical topics
* User authentication
* Saved reports and conversations
* Medical report history
* Voice input
* Voice responses
* More Indian regional languages
* Improved accessibility
* Cloud deployment
* Mobile-friendly interface

---

## 👨‍💻 Project

**Project Name:** MedExplain AI

**Purpose:** AI-powered medical education and information assistance

**Technology:** Python + Streamlit + Groq

---

## 📜 Disclaimer

MedExplain AI provides AI-generated educational information. AI responses may contain errors or incomplete information. Always consult an appropriately qualified healthcare professional for medical decisions.
