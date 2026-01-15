import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat
from components.image_uploader import render_image_uploader


st.set_page_config(page_title="AI Medical Assistant", layout="wide")

# Loader Injection
st.markdown("""
<div class="loader-container">
    <div class="loader-content">
        <div class="dna-spinner"></div>
        <div class="loader-text">INITIALIZING MEDI-CORE...</div>
    </div>
</div>
""", unsafe_allow_html=True)
# st.title(" 🩺 Medical Assistant Chatbot") # Replaced by custom HTML above

# Web3/Cyberpunk Design Injection with Red Accents
st.markdown("""
    <style>
        /* LOADER ANIMATION */
        .loader-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #000;
            z-index: 99999;
            display: flex;
            justify-content: center;
            align-items: center;
            animation: fadeOut 1s ease-in-out 3s forwards;
            pointer-events: none;
        }
        
        .loader-content {
            text-align: center;
        }
        
        .dna-spinner {
            width: 80px;
            height: 80px;
            border: 5px solid rgba(57, 255, 20, 0.2);
            border-top: 5px solid #39ff14;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px auto;
            box-shadow: 0 0 20px rgba(57, 255, 20, 0.5);
        }
        
        .loader-text {
            font-family: 'Courier New', monospace;
            color: #39ff14;
            font-size: 1.5rem;
            letter-spacing: 5px;
            animation: pulse 1.5s infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @keyframes fadeOut {
            0% { opacity: 1; }
            100% { opacity: 0; visibility: hidden; }
        }
        
        @keyframes pulse {
            0% { opacity: 0.5; }
            50% { opacity: 1; }
            100% { opacity: 0.5; }
        }

        /* GLOBAL BACKGROUND IMAGE */
        .stApp {
            background-color: #050505;
            background-image: 
                linear-gradient(rgba(57, 255, 20, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(57, 255, 20, 0.1) 1px, transparent 1px),
                radial-gradient(circle at 50% 0%, rgba(57, 255, 20, 0.25) 0%, transparent 60%),
                radial-gradient(circle at 85% 30%, rgba(255, 170, 0, 0.2) 0%, transparent 50%),
                linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
            background-size: 40px 40px, 40px 40px, cover, cover, cover;
            background-attachment: fixed;
            color: #e0e0e0;
            font-family: 'Inter', sans-serif;
        }
        
        /* Dark overlay to ensure text readability */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85); /* 85% opacity black overlay */
            pointer-events: none;
            z-index: 0;
        }

        /* Sidebar - Glassmorphism */
        section[data-testid="stSidebar"] {
            background: rgba(10, 10, 10, 0.6) !important;
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(57, 255, 20, 0.1);
            box-shadow: 5px 0 20px rgba(57, 255, 20, 0.05);
        }

        /* Main Title - Red Neon */
        /* Main Title - Green Neon */
        h1 {
            color: #39ff14 !important;
            text-align: center;
            text-shadow: 
                0 0 10px rgba(57, 255, 20, 0.8), 
                0 0 20px rgba(57, 255, 20, 0.6),
                0 0 40px rgba(57, 255, 20, 0.4);
            font-weight: 900;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 2rem;
        }
        
        /* Subheaders - Orange */
        h2, h3, h4, h5, h6 {
            color: #ffaa00 !important;
            font-weight: 600;
        }

        /* Button Styling - Red & Green Neon */
        /* Button Styling - Green Neon */
        .stButton button {
            background: rgba(57, 255, 20, 0.1);
            color: #39ff14;
            border: 1px solid #39ff14;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .stButton button:hover {
            background: #39ff14;
            color: #000;
            box-shadow: 0 0 20px #39ff14;
            transform: translateY(-2px);
        }

        /* Input Fields */
        .stTextInput input {
            background-color: rgba(255, 255, 255, 0.05);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
        }
        .stTextInput input:focus {
             border: 1px solid #ffaa00;
             color: #ffaa00;
        }

        /* File Uploader area */
        section[data-testid="stFileUploader"] {
            background-color: rgba(20, 20, 20, 0.5);
            border-radius: 12px;
            padding: 30px;
            border: 2px dashed rgba(57, 255, 20, 0.5);
            transition: border-color 0.3s;
        }
        section[data-testid="stFileUploader"]:hover {
            border-color: #39ff14;
            background-color: rgba(57, 255, 20, 0.05);
        }
        section[data-testid="stFileUploader"] button {
             border: 1px solid #39ff14;
             color: #39ff14;
        }


        /* Chat Messages */
        .stChatMessage {
            background-color: rgba(25, 25, 25, 0.8);
            border-radius: 15px;
            border: 1px solid rgba(57, 255, 20, 0.1);
            backdrop-filter: blur(10px);
            margin-bottom: 15px;
        }
        .stChatMessage[data-testid="chatAvatarIcon-user"] {
             background-color: #39ff14;
             color: black;
        }
        div[data-testid="stMarkdownContainer"] p {
            font-size: 1.05rem;
            line-height: 1.6;
        }

        /* Horizontal Rule Neon */
        hr {
            border-top: 2px solid #39ff14;
            margin: 2em 0;
            opacity: 0.5;
            box-shadow: 0 0 10px #39ff14;
        }
        
        /* Mobile Responsiveness Improvements */
        @media (max-width: 640px) {
            h1 {
                font-size: 1.8rem !important;
                margin-top: 1rem;
            }
            .stButton button {
                width: 100%;
                margin-bottom: 10px;
            }
            section[data-testid="stSidebar"] {
                width: 100% !important;
            }
        }

        /* --------------------------
           WEB3 SLIDER / CAROUSEL CSS 
           -------------------------- */
        .scrolling-wrapper {
            display: flex;
            flex-wrap: nowrap;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            padding: 30px 20px; /* Safe padding */
            gap: 25px;
            scrollbar-width: thin;
            scrollbar-color: #39ff14 #1a1a1a;
            /* Removed centering properties to fix left-cutoff issue */
        }
        
        .card {
            flex: 0 0 auto;
            width: 280px;
            height: 260px; /* Increased height further */
            background: rgba(20, 20, 20, 0.8);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 25px;
            padding-bottom: 40px; /* Added bottom padding to keep text away from bottom edge */
            color: #fff;
            position: relative;
            overflow: hidden;
            transition: all 0.4s ease;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            text-align: left; /* Ensures internal content is preserved at left */
        }
        
        /* Unique Colors for Cards */
        .card:nth-child(1) { --card-glow: #00f2ff; } /* Cyan */
        .card:nth-child(2) { --card-glow: #bc13fe; } /* Purple */
        .card:nth-child(3) { --card-glow: #39ff14; } /* Neon Green */
        .card:nth-child(4) { --card-glow: #ffae00; } /* Gold */
        .card:nth-child(5) { --card-glow: #ff0055; } /* Pink */

        .card:hover {
            transform: translateY(-8px) scale(1.02);
            border-color: var(--card-glow);
            box-shadow: 0 10px 40px rgba(0,0,0,0.5), 
                        0 0 20px var(--card-glow); /* Dynamic glow based on card color */
            background: rgba(30,30,30, 0.9);
        }

        .card h3 {
            font-size: 1.3rem;
            margin-bottom: 15px; /* Added margin */
            color: #e0e0e0 !important;
            transition: color 0.3s;
        }
        .card:hover h3 {
            color: var(--card-glow) !important;
        }
        
        .card p {
            font-size: 0.95rem; /* Slight increase for readability */
            opacity: 0.8;
            margin: 0;
            line-height: 1.6;
        }
        
        .card .icon {
            font-size: 2.5rem; /* Larger icons */
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255,255,255,0.3);
        }
        
        /* Neon bar indicator at bottom of card */
        .card::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, transparent, var(--card-glow), transparent);
            opacity: 0.5;
            transition: opacity 0.3s;
        }
        .card:hover::after {
            opacity: 1;
            box-shadow: 0 0 10px var(--card-glow);
        }
        
        /* Hide Streamlit Deploy Button and Menu */
        .stAppDeployButton {
            display: none;
            visibility: hidden;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* ADVANCED FOOTER STYLING */
        .advanced-footer {
            margin-top: 100px;
            padding: 40px 40px; /* Reduced vertical padding */
            background: #080808;
            border-top: 1px solid #333;
            color: #aaa;
            font-family: 'Inter', sans-serif;
        }
        
        /* ... skipped grid styles ... */

        .footer-bottom {
            margin-top: 20px; /* Drastically reduced from 60px */
            padding-top: 20px;
            border-top: 1px solid #222;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            font-size: 0.8rem;
            color: #666;
        }
            border-top: 1px solid #222;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            font-size: 0.8rem;
            color: #666;
        }
        
        .social-row {
            display: flex;
            gap: 15px;
        }
        .social-row i {
            font-size: 1.2rem;
            color: #888;
            transition: 0.3s;
            cursor: pointer;
        }
        .social-row i:hover {
            color: #39ff14;
        }

    </style>
    <!-- Add FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""", unsafe_allow_html=True)


# Custom Header with Icon and Animation
st.markdown("""
<div style="text-align: center; padding: 40px 20px 20px 20px;">
    <h1 style='margin:0; font-size: 4rem; text-shadow: 0 0 20px rgba(57, 255, 20, 0.5);'>
        🩺 <span style="color:#ffffff;">MEDI</span><span style="color:#39ff14;">CORE</span>
    </h1>
</div>
""", unsafe_allow_html=True)

# WEB3 Card Slider Component
st.markdown("""
<div class="scrolling-wrapper">
    <div class="card">
        <div class="icon">🔬</div>
        <h3>Image Analysis</h3>
        <p>Precision diagnostics using computer vision to detect anomalies in X-rays & MRIs.</p>
    </div>
    <div class="card">
        <div class="icon">🤖</div>
        <h3>AI Diagnosis</h3>
        <p>Instant second opinions backed by millions of clinical records.</p>
    </div>
    <div class="card">
        <div class="icon">📑</div>
        <h3>Report Genius</h3>
        <p>Turn complex medical PDFs into clear, actionable summaries instantly.</p>
    </div>
    <div class="card">
        <div class="icon">🔒</div>
        <h3>Secure & Private</h3>
        <p>HIPAA-compliant safeguards ensuring your health data remains confidential.</p>
    </div>
    <div class="card">
        <div class="icon">⚡</div>
        <h3>Real-time Chat</h3>
        <p>24/7 Medical Assistant ready to answer your health queries.</p>
    </div>
</div>
""", unsafe_allow_html=True)




render_uploader()
render_chat()
render_image_uploader()
render_history_download()


# NTT Data Style Footer Component
st.markdown("""
<style>
/* Footer Container */
.ntt-footer {
background-color: #060912; /* Reduced dark blue (closer to black) */
color: #ffffff;
padding: 30px 40px;
font-family: 'Inter', sans-serif;
font-size: 13px;
margin-top: 0px;
border-top: 1px solid #1e2b45;
border-radius: 20px; /* Curve for 4 sides */
margin-bottom: 20px; /* Space for the curve to be visible at bottom */
}


/* Top Section */
.footer-top {
display: flex;
justify-content: space-between;
align-items: center;
margin-bottom: 30px;
border-bottom: 1px solid #1e2b45;
padding-bottom: 20px;
}
.footer-logo {
font-size: 1.4rem;
font-weight: bold;
display: flex;
align-items: center;
gap: 10px;
}
.footer-logo span { font-family: 'Orbitron', sans-serif; }
.global-select { font-size: 0.85rem; opacity: 0.8; cursor: pointer; }
/* Middle Section */
.footer-links-grid {
display: grid;
grid-template-columns: repeat(4, 1fr);
gap: 20px;
margin-bottom: 30px;
}
.footer-col h4 {
font-size: 0.9rem;
font-weight: 700;
margin-bottom: 15px;
color: #fff;
text-transform: uppercase;
}
.footer-col ul { list-style: none; padding: 0; margin: 0; }
.footer-col ul li { margin-bottom: 10px; }
.footer-col ul li a {
color: #b0b0b0;
text-decoration: none;
transition: color 0.3s;
}
.footer-col ul li a:hover { color: #fff; text-decoration: underline; }
/* Subscribe Section */
.subscribe-wrapper {
background: #121d33;
padding: 20px;
border-radius: 8px;
margin-bottom: 30px;
display: flex;
align-items: center;
justify-content: space-between;
flex-wrap: wrap;
gap: 20px;
border: 1px solid #1e2b45;
}
.subscribe-text h5 { margin: 0 0 5px 0; font-size: 1rem; color: #fff; }
.subscribe-text p { margin: 0; color: #aaa; font-size: 0.8rem; }
.subscribe-form { display: flex; gap: 10px; }
.subscribe-form input {
background: #0b1426;
border: 1px solid #2a3b55;
padding: 8px 12px;
color: #fff;
border-radius: 4px;
outline: none;
}
.subscribe-form button {
background: #0066cc;
color: #fff;
border: none;
padding: 8px 20px;
border-radius: 4px;
cursor: pointer;
font-weight: bold;
}
.subscribe-form button:hover { background: #005bb5; }
/* Bottom Section */
.footer-bottom {
display: flex;
flex-direction: column;
gap: 20px;
}
.legal-links {
display: flex;
gap: 20px;
flex-wrap: wrap;
font-size: 0.8rem;
color: #777;
padding-bottom: 20px;
border-bottom: 1px solid #1e2b45;
}
.legal-links a { color: #777; text-decoration: none; }
.legal-links a:hover { color: #fff; }
.bottom-row {
display: flex;
justify-content: space-between;
align-items: center;
padding-top: 15px;
gap: 20px; /* Prevent overlap */
flex-wrap: wrap;
}
.social-icons-row { display: flex; gap: 15px; }
.social-icons-row i {
font-size: 1.1rem;
color: #aaa;
cursor: pointer;
transition: 0.3s;
}
.social-icons-row i:hover { color: #fff; transform: translateY(-2px); }
.copyright-text { color: #555; font-size: 0.75rem; }
/* Responsive */
@media (max-width: 768px) {
.footer-links-grid { grid-template-columns: 1fr 1fr; }
.subscribe-wrapper { flex-direction: column; align-items: flex-start; }
.bottom-row { flex-direction: column; align-items: flex-start; gap: 15px; }
}
</style>
<div class="ntt-footer">
<div class="footer-top">
<div class="footer-logo">
<i class="fas fa-circle-notch"></i> <span>MEDI DATA</span>
</div>
<div class="global-select">
<i class="fas fa-globe"></i> Global | Select a Country
</div>
</div>
<div class="footer-links-grid">
<div class="footer-col">
<h4>Industries</h4>
<ul>
<li><a href="#">Healthcare</a></li>
<li><a href="#">Automotive</a></li>
<li><a href="#">Finance</a></li>
<li><a href="#">Public Sector</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Services</h4>
<ul>
<li><a href="#">Cloud</a></li>
<li><a href="#">Data & AI</a></li>
<li><a href="#">Consulting</a></li>
<li><a href="#">Cybersecurity</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Insights</h4>
<ul>
<li><a href="#">Case Studies</a></li>
<li><a href="#">Blog</a></li>
<li><a href="#">Research</a></li>
</ul>
</div>
<div class="footer-col">
<h4>About Us</h4>
<ul>
<li><a href="#">Careers</a></li>
<li><a href="#">Investors</a></li>
<li><a href="#">News</a></li>
<li><a href="#">Sustainability</a></li>
</ul>
</div>
</div>
<div class="subscribe-wrapper">
<div class="subscribe-text">
<h5>Stay Updated</h5>
<p>Get the latest news and insights delivered to your inbox.</p>
</div>
<div class="subscribe-form">
<input type="email" placeholder="Email address">
<button>Subscribe</button>
</div>
</div>
<div class="footer-bottom">
<div class="legal-links">
<a href="#">Sitemap</a>
<a href="#">Privacy</a>
<a href="#">Terms</a>
<a href="#">Accessibility</a>
<a href="#">Cookies</a>
</div>
<div class="bottom-row">
<div class="social-icons-row">
<i class="fab fa-x-twitter"></i>
<i class="fab fa-instagram"></i>
<i class="fab fa-linkedin-in"></i>
<i class="fab fa-youtube"></i>
</div>
<div class="copyright-text">
Copyright © 2026 MEDI DATA Group.
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
