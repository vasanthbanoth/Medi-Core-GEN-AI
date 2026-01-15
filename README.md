# Medi-Core Gen AI 🩺

A Multimodal Medical AI Assistant powered by **Google Gemini 2.0** and **Streamlit**.

## 🚀 Features
- **👁️ Visual Analysis**: Upload medical images (X-Rays, handwritten prescriptions) and get instant explanations using **Google Gemini 2.0 Flash** (with auto-fallback to stable versions).
- **💬 Interactive Chat**: Ask follow-up questions about the analyzed images.
- **🎨 Modern UI**: A "Web3/Cyberpunk" styled interface built entirely in Python.
- **☁️ Cloud/Mobile Ready**: Optimized for Streamlit Cloud (No Docker/Server required).

## 📖 The Implementation Story
Want to know how this was built from scratch? Check out the included notebook:
- **[MediCore_Implementation_Story.ipynb](MediCore_Implementation_Story.ipynb)**: A step-by-step guide explaining:
    - Why we chose **Gemini** over other models.
    - How **RAG** (Retrieval Augmented Generation) works conceptually.
    - Why **Streamlit** was the perfect choice for the frontend.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash / 1.5 Flash (via `google-generativeai`)
- **Language**: Python 3.14+

---

## ⚡ Quick Start

### Run Locally

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd Medi-Core-Gen-AI-main
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r medicore-main/client/requirements.txt
    ```

3.  **Configure API Key**:
    Create `medicore-main/client/.env` and add your Google Key:
    ```env
    GOOGLE_API_KEY="your_api_key_here"
    ```

4.  **Run the App**:
    ```bash
    streamlit run medicore-main/client/app.py
    ```
    Open **http://localhost:8501** in your browser.

---

## 📂 Project Structure
```
Medi-Core-Gen-AI-main/
├── medicore-main/
│   ├── client/          # Main Application
│   │   ├── app.py       # Entry Point
│   │   ├── utils/       # AI Logic (api.py)
│   │   └── components/  # UI Modules
├── MediCore_Implementation_Story.ipynb  # The "Behind the Scenes" Story
└── README.md
```
