# Medi-Core Gen AI 🩺

A Multimodal Medical AI Assistant powered by **Google Gemini** and **Streamlit**.

## 🚀 Features
- **👁️ Visual Analysis**: Upload medical images (X-Rays, handwritten prescriptions) and get instant explanations using **Google Gemini 2.0 Flash**.
- **💬 Interactive Chat**: Ask follow-up questions about the analyzed images.
- **🎨 Modern UI**: A "Web3/Cyberpunk" styled interface built entirely in Python.
- **🐳 Dockerized**: Ready for deployment on AWS with a single command.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Model**: Google Gemini (via `google-generativeai`)
- **Containerization**: Docker & Docker Compose

---

## ⚡ Quick Start

### Option 1: Run with Docker (Recommended)
The easiest way to run the full stack (Frontend + Backend).

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd Medi-Core-Gen-AI-main
    ```

2.  **Configure API Key**:
    Create `medicore-main/server/.env` and add your Google Key:
    ```env
    GOOGLE_API_KEY=AIzaSy...
    ```

3.  **Run**:
    ```bash
    docker-compose up --build
    ```
    Open **http://localhost:8501** in your browser.

---

### Option 2: Run Locally (For Development)

#### 1. Start the Backend
```bash
cd medicore-main/server
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

#### 2. Start the Frontend
Open a new terminal:
```bash
cd medicore-main/client
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure
```
Medi-Core-Gen-AI-main/
├── medicore-main/
│   ├── client/          # Streamlit Fronend
│   │   ├── app.py       # Main UI logic
│   │   └── Dockerfile
│   ├── server/          # FastAPI Backend
│   │   ├── main.py      # API Routes
│   │   ├── modules/     # AI Logic (Gemini Handler)
│   │   └── Dockerfile
│   └── docker-compose.yml
├── aws_setup_guide.md   # Deployment Instructions
└── README.md
```
