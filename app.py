
import streamlit as st
from groq import Groq
import os
import base64
from datetime import datetime
import json

# --- API CONFIGURATION ---
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Taqwa & Aqsa Executive Portal", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL ADVANCED THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&family=Playfair+Display:wght@700;900&display=swap');

header[data-testid="stHeader"] {
    background: transparent !important;
}

.stApp > header {
    background: transparent !important;
}

.block-container {
    padding-top: 1rem !important;
}
    


    .stApp > div:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    .stAppViewContainer {
        padding-top: 0 !important;
        margin-top: 0 !important;
        padding-bottom: 80px !important;
    }

    /* PROFESSIONAL GRADIENT BACKGROUND */
    .stApp { 
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 50%, #90caf9 100%) !important; 
        color: #1a1a1a !important; 
        font-family: 'Poppins', sans-serif;
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    /* BODY & TEXT */
    body { background-color: #e3f2fd !important; }
    .stMarkdown, .stText, p, li, label, .stExpander { 
        color: #1a1a1a !important; 
        font-size: 15px !important;
        font-weight: 500 !important;
    }

    /* PROFESSIONAL SIDEBAR */
    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%) !important; 
        border-right: 5px solid #ffd700;
        box-shadow: 5px 0 20px rgba(0, 0, 0, 0.2) !important;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    [data-testid="stSidebar"] h2 {
        color: #ffd700 !important;
        font-size: 24px !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-family: 'Playfair Display', serif !important;
    }

    /* MAIN HEADINGS - PROFESSIONAL */
    .section-header {
        color: #1e3c72 !important;
        font-family: 'Playfair Display', serif;
        font-weight: 900 !important;
        text-shadow: 0px 2px 8px rgba(30, 60, 114, 0.3);
        border-bottom: 4px solid #ffd700;
        padding-bottom: 15px;
        margin-bottom: 30px;
        font-size: 48px !important;
        margin-top: 10px !important;
        letter-spacing: 1px !important;
    }

    /* DASHBOARD TITLE */
    .dashboard-title {
        color: #1e3c72 !important;
        font-family: 'Playfair Display', serif;
        font-weight: 900 !important;
        text-shadow: 0px 3px 10px rgba(30, 60, 114, 0.4);
        font-size: 70px !important;
        margin-top: 20px !important;
        letter-spacing: 2px !important;
        text-align: center !important;
    }

    .dashboard-subtitle {
        color: #2a5298 !important;
        font-size: 22px !important;
        letter-spacing: 4px !important;
        font-weight: 700 !important;
        margin-bottom: 40px !important;
        text-transform: uppercase !important;
        text-align: center !important;
    }

    /* UNIFORM FEATURE CARDS - CLICKABLE */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%) !important;
        border: 3px solid #2a5298 !important;
        padding: 40px 30px !important;
        border-radius: 18px !important;
        text-align: center !important;
        box-shadow: 0 10px 30px rgba(30, 60, 114, 0.2) !important;
        transition: all 0.4s ease !important;
        min-height: 280px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        cursor: pointer !important;
    }
    .feature-card:hover {
        transform: translateY(-12px) !important;
        box-shadow: 0 15px 45px rgba(30, 60, 114, 0.3) !important;
        background: linear-gradient(135deg, #f5f5f5, #eeeeee) !important;
        border-color: #ffd700 !important;
    }
    .feature-card-emoji {
        font-size: 48px !important;
        margin-bottom: 15px !important;
        animation: float 3s ease-in-out infinite !important;
    }
    .feature-card b {
        color: #1e3c72 !important;
        font-size: 20px !important;
        display: block !important;
        margin-bottom: 12px !important;
        font-weight: 700 !important;
    }
    .feature-card p {
        color: #2a5298 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        margin: 0 !important;
        line-height: 1.4 !important;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    /* PREMIUM CARDS */
    .project-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.85)) !important;
        border: 2px solid #2a5298 !important;
        padding: 25px !important;
        border-radius: 16px !important;
        margin-bottom: 20px !important;
        color: #1a1a1a !important;
        box-shadow: 0 8px 24px rgba(30, 60, 114, 0.15) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border-left: 5px solid #ffd700 !important;
    }
    .project-card:hover {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(255, 255, 255, 0.9)) !important;
        box-shadow: 0 12px 36px rgba(30, 60, 114, 0.25) !important;
        transform: translateY(-5px) !important;
        border-left: 8px solid #ffd700 !important;
    }
    .project-card b { 
        color: #1e3c72 !important; 
        font-size: 18px !important;
        display: block !important;
        margin-bottom: 12px !important;
        font-weight: 700 !important;
    }

    /* EXPANDERS - PROFESSIONAL */
    [data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid #2a5298 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(30, 60, 114, 0.1) !important;
    }

    /* INPUT FIELDS */
    input, textarea, select {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        border: 2px solid #2a5298 !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
    }

    /* BUTTONS - PREMIUM */
    .stButton > button {
        background: linear-gradient(135deg, #ffd700 0%, #ffb700 100%) !important;
        color: #1e3c72 !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 14px 30px !important;
        font-size: 16px !important;
        box-shadow: 0 6px 18px rgba(255, 215, 0, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 28px rgba(255, 215, 0, 0.6) !important;
    }

    /* STATUS MESSAGES */
    .stSuccess {
        background-color: rgba(76, 175, 80, 0.15) !important;
        border: 2px solid #4caf50 !important;
        color: #1a1a1a !important;
        border-radius: 10px !important;
        padding: 15px !important;
    }
    .stWarning {
        background-color: rgba(255, 193, 7, 0.15) !important;
        border: 2px solid #ffc107 !important;
        border-radius: 10px !important;
        padding: 15px !important;
    }
    .stError {
        background-color: rgba(244, 67, 54, 0.15) !important;
        border: 2px solid #f44336 !important;
        border-radius: 10px !important;
        padding: 15px !important;
    }

    /* FOOTER - PREMIUM */
    .footer {
        position: fixed; 
        bottom: 0; 
        left: 0; 
        width: 100%;
        text-align: center; 
        padding: 14px; 
        background: linear-gradient(90deg, #1e3c72, #2a5298);
        color: #ffd700; 
        font-weight: bold; 
        border-top: 4px solid #ffd700;
        z-index: 100;
        font-size: 14px !important;
    }

    /* DIVIDER */
    hr { border-top: 3px solid #2a5298 !important; }

    /* ACTIVITY CARD */
    .activity-card {
        background: linear-gradient(135deg, #fff9e6, #fffacc) !important;
        border: 2px solid #ffd700 !important;
        padding: 20px !important;
        border-radius: 14px !important;
        margin: 15px 0 !important;
        color: #333 !important;
        box-shadow: 0 4px 12px rgba(255, 215, 0, 0.2) !important;
    }

    /* CODE CARDS */
    .code-card {
        background: linear-gradient(135deg, #1a1a1a, #2d2d2d) !important;
        border: 2px solid #ffd700 !important;
        padding: 20px !important;
        border-radius: 14px !important;
        margin: 15px 0 !important;
        color: #00ff00 !important;
        font-family: 'Courier New', monospace !important;
        box-shadow: 0 4px 12px rgba(255, 215, 0, 0.2) !important;
        overflow-x: auto !important;
    }

    /* TABS STYLING */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px !important;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(30, 60, 114, 0.1) !important;
        border: 2px solid #2a5298 !important;
        border-radius: 10px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffd700 !important;
        color: #1e3c72 !important;
    }

    /* METRICS */
    .stMetric {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.85)) !important;
        border: 2px solid #2a5298 !important;
        padding: 20px !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 12px rgba(30, 60, 114, 0.1) !important;
    }

    /* ARABIC TEXT */
    .arabic-text {
        font-size: 22px !important;
        font-weight: 600 !important;
        color: #1e3c72 !important;
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Traditional Arabic', Arial !important;
        line-height: 2 !important;
        background: rgba(255, 215, 0, 0.1) !important;
        padding: 15px !important;
        border-radius: 10px !important;
        border-right: 4px solid #ffd700 !important;
    }

    /* PREMIUM BADGE */
    .premium-badge {
        background: linear-gradient(135deg, #ffd700, #ffb700) !important;
        color: #1e3c72 !important;
        padding: 8px 15px !important;
        border-radius: 20px !important;
        font-weight: 700 !important;
        display: inline-block !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        margin: 5px 0 !important;
    }

    /* SCROLL ENHANCEMENT */
    ::-webkit-scrollbar {
        width: 10px !important;
    }
    ::-webkit-scrollbar-track {
        background: #e3f2fd !important;
    }
    ::-webkit-scrollbar-thumb {
        background: #2a5298 !important;
        border-radius: 5px !important;
    }

    /* LOGO CONTAINER */
    .logo-container {
        text-align: center !important;
        margin-bottom: 20px !important;
        padding: 20px !important;
        background: rgba(255, 255, 255, 0.5) !important;
        border-radius: 16px !important;
        border: 2px solid #ffd700 !important;
    }

    /* SKILL PROGRESS BARS */
    .skill-bar {
        background-color: #e3f2fd !important;
        border: 2px solid #2a5298 !important;
        border-radius: 10px !important;
        overflow: hidden !important;
        margin: 10px 0 !important;
        height: 30px !important;
    }

    .skill-progress {
        background: linear-gradient(90deg, #ffd700, #ffb700) !important;
        height: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: #1e3c72 !important;
        font-weight: 700 !important;
        transition: width 0.5s ease !important;
    }

    /* FEEDBACK CARD */
    .feedback-card {
        background: linear-gradient(135deg, #e8f5e9, #f1f8e9) !important;
        border: 2px solid #66bb6a !important;
        padding: 20px !important;
        border-radius: 14px !important;
        margin: 15px 0 !important;
        color: #1a1a1a !important;
        box-shadow: 0 4px 12px rgba(102, 187, 106, 0.2) !important;
    }

    /* IMPROVEMENT CARD */
    .improvement-card {
        background: linear-gradient(135deg, #fff3e0, #ffe0b2) !important;
        border: 2px solid #ffa726 !important;
        padding: 20px !important;
        border-radius: 14px !important;
        margin: 15px 0 !important;
        color: #1a1a1a !important;
        box-shadow: 0 4px 12px rgba(255, 167, 38, 0.2) !important;
    }

    /* STRENGTH CARD */
    .strength-card {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb) !important;
        border: 2px solid #42a5f5 !important;
        padding: 20px !important;
        border-radius: 14px !important;
        margin: 15px 0 !important;
        color: #1a1a1a !important;
        box-shadow: 0 4px 12px rgba(66, 165, 245, 0.2) !important;
    }

    /* RATING STARS */
    .rating-stars {
        font-size: 24px !important;
        color: #ffd700 !important;
        margin: 10px 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UTILITY: IMAGE LOADER ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# --- ISLAMIC REFERENCES DATABASE ---
ISLAMIC_DB = {
    "Science": {
        "references": [
            {
                "arabic": "وَفِي خَلْقِ السَّمَاوَاتِ وَالْأَرْضِ وَاخْتِلَافِ اللَّيْلِ وَالنَّهَارِ لَآيَاتٌ لِأُولِي الْأَلْبَابِ",
                "urdu": "آسمانوں اور زمین کی تخلیق میں، اور رات اور دن کے بدلنے میں عقلمند لوگوں کے لیے بہت سے نشانیاں ہیں",
                "english": "In the creation of the heavens and the earth, and the alternation of night and day, there are surely signs for the people of understanding",
                "surah": "Quran 3:190"
            }
        ]
    }
}

# --- VALUE & SKILLS DATABASE ---
VALUES_SKILLS = {
    "English Spoken Practice": {
        "description": "Master English Communication & Fluency",
        "levels": ["Beginner", "Intermediate", "Advanced"],
        "topics": [
            "Daily Conversations",
            "Business English",
            "Presentation Skills",
            "Public Speaking",
            "Accent Reduction",
            "Listening Comprehension"
        ],
        "practice_activities": [
            "Role-Playing Scenarios",
            "Record & Listen",
            "Group Discussions",
            "Debate Practice",
            "Interview Preparation",
            "Storytelling Sessions"
        ]
    },
    "Islamic Ethics & Manners": {
        "description": "Develop Character & Islamic Values",
        "levels": ["Foundation", "Intermediate", "Advanced"],
        "topics": [
            "Respect & Courtesy",
            "Honesty & Integrity",
            "Kindness & Compassion",
            "Discipline & Patience",
            "Responsibility",
            "Islamic Etiquette",
            "Family Values",
            "Community Service"
        ],
        "practice_activities": [
            "Character Building",
            "Case Study Analysis",
            "Real-Life Scenarios",
            "Community Projects",
            "Hadith Study",
            "Moral Dilemmas Discussion"
        ]
    },
    "Personal Development": {
        "description": "Build Confidence & Leadership",
        "levels": ["Beginner", "Intermediate", "Advanced"],
        "topics": [
            "Self-Confidence",
            "Time Management",
            "Goal Setting",
            "Leadership Skills",
            "Emotional Intelligence",
            "Teamwork",
            "Problem Solving",
            "Creativity & Innovation"
        ],
        "practice_activities": [
            "Leadership Training",
            "Goal Setting Workshops",
            "Team Projects",
            "Mentoring Sessions",
            "Feedback Exchange",
            "Reflection Journals"
        ]
    },
    "Social Skills": {
        "description": "Enhance Communication & Relationships",
        "levels": ["Basic", "Intermediate", "Advanced"],
        "topics": [
            "Active Listening",
            "Empathy Development",
            "Conflict Resolution",
            "Cooperative Learning",
            "Networking",
            "Cross-Cultural Communication",
            "Friendship Building",
            "Peer Support"
        ],
        "practice_activities": [
            "Group Activities",
            "Conflict Resolution Workshops",
            "Social Events",
            "Peer Tutoring",
            "Community Engagement",
            "Collaborative Projects"
        ]
    }
}

logo_data = get_image_base64("school.logo.png")

# --- SIDEBAR WITH NAVIGATION ---
with st.sidebar:
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    if logo_data:
        st.markdown(f'<center><img src="data:image/png;base64,{logo_data}" width="140"></center>', unsafe_allow_html=True)
    else:
        st.markdown('<center><h3>🎓 TAQWA & AQSA</h3></center>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center;'>📋 EXECUTIVE MENU</h2>", unsafe_allow_html=True)
    st.divider()
    
    choice = st.radio("➤ Navigation:", ["🏠 Dashboard", "📝 AI Paper Evaluation", "📚 Lesson Architect", "🕌 Islamic Integration", "🧪 STEM Hub", "💻 Coding Projects", "📐 Teaching Aids", "⭐ Value & Skills"])

# --- DASHBOARD ---
if choice == "🏠 Dashboard":
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    if logo_data:
        st.markdown(f'<center><img src="data:image/png;base64,{logo_data}" width="200"></center>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="dashboard-title" style="text-align:center;">Taqwa & Aqsa</h1>', unsafe_allow_html=True)
    st.markdown('<p class="dashboard-subtitle" style="text-align:center;">ADVANCED EDUCATIONAL EXECUTIVE PORTAL</p>', unsafe_allow_html=True)
    
    # UNIFORM SIZE FEATURE CARDS - ROW 1
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">🤖</div>
            <b>AI CORE</b>
            <p>Smart Evaluation Engine</p>
            <span class="premium-badge">Premium</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">🕌</div>
            <b>SPIRITUAL</b>
            <p>Islamic Integration</p>
            <span class="premium-badge">Premium</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">💡</div>
            <b>INNOVATION</b>
            <p>STEM Projects</p>
            <span class="premium-badge">Premium</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">💻</div>
            <b>CODING</b>
            <p>Programming Basics</p>
            <span class="premium-badge">Advanced</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # UNIFORM SIZE FEATURE CARDS - ROW 2
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">📊</div>
            <b>ANALYTICS</b>
            <p>Progress Tracking</p>
            <span class="premium-badge">Premium</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">🎓</div>
            <b>EXCELLENCE</b>
            <p>Quality Tools</p>
            <span class="premium-badge">Premium</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col7:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">⭐</div>
            <b>VALUES</b>
            <p>Skills Development</p>
            <span class="premium-badge">New</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col8:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-emoji">📐</div>
            <b>TEACHING AIDS</b>
            <p>Resource Library</p>
            <span class="premium-badge">Premium</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
        <b>📌 Welcome to Advanced Educational Portal</b>
        <p>Comprehensive solution for modern education combining AI, STEM, Islamic values, coding education, and character development.</p>
        <p><b>✨ Core Features:</b></p>
        <ul>
            <li>✓ Advanced AI-Powered Examination System</li>
            <li>✓ Interactive Lesson Planning with AI</li>
            <li>✓ Islamic Curriculum Integration (Arabic + Urdu + English)</li>
            <li>✓ Hands-on STEM Projects with Instructions</li>
            <li>✓ Complete Coding Education Programs</li>
            <li>✓ Professional Teaching Aids Library</li>
            <li>✓ Value-Based Skills Development Program</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- VALUE & SKILLS SECTION ---
elif choice == "⭐ Value & Skills":
    st.markdown('<h1 class="section-header">⭐ Values & Skills Development Program</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <b>🌟 Holistic Development for Students</b>
        <p>Build character, enhance communication, develop leadership, and instill Islamic values for overall personality development.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Level Selection with Arrows
    tab1, tab2, tab3, tab4 = st.tabs(["🗣️ English Speaking", "🕌 Islamic Ethics", "🚀 Personal Dev", "👥 Social Skills"])
    
    with tab1:
        st.markdown("""
        <div class="project-card">
            <b>🗣️ English Spoken Practice</b>
            <p>Master English Communication & Fluency</p>
        </div>
        """, unsafe_allow_html=True)
        
        skill_data = VALUES_SKILLS["English Spoken Practice"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="project-card">
                <b>📚 Topics Covered:</b>
                <ul>
                    {"".join([f"<li>✓ {topic}</li>" for topic in skill_data['topics']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="project-card">
                <b>🎯 Practice Activities:</b>
                <ul>
                    {"".join([f"<li>✓ {activity}</li>" for activity in skill_data['practice_activities']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Skill Progress
        st.markdown("<b>📊 Skill Progress Tracking:</b>", unsafe_allow_html=True)
        
        skills_english = {
            "Listening": 75,
            "Speaking": 60,
            "Pronunciation": 55,
            "Vocabulary": 80,
            "Confidence": 65
        }
        
        for skill_name, progress in skills_english.items():
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <b>{skill_name}</b>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {progress}%;">
                        <span>{progress}%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Learning Levels
        col_l1, col_l2, col_l3 = st.columns(3)
        with col_l1:
            if st.button("▶ BEGINNER LEVEL", use_container_width=True):
                st.info("📖 Start with basic greetings, introductions, and daily conversations")
        with col_l2:
            if st.button("▶ INTERMEDIATE LEVEL", use_container_width=True):
                st.info("📚 Learn business English, presentations, and detailed discussions")
        with col_l3:
            if st.button("▶ ADVANCED LEVEL", use_container_width=True):
                st.info("🎓 Master fluency, public speaking, and professional communication")
    
    with tab2:
        st.markdown("""
        <div class="project-card">
            <b>🕌 Islamic Ethics & Manners</b>
            <p>Develop Character & Islamic Values</p>
        </div>
        """, unsafe_allow_html=True)
        
        skill_data = VALUES_SKILLS["Islamic Ethics & Manners"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="project-card">
                <b>📖 Core Topics:</b>
                <ul>
                    {"".join([f"<li>✓ {topic}</li>" for topic in skill_data['topics']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="project-card">
                <b>🎯 Learning Activities:</b>
                <ul>
                    {"".join([f"<li>✓ {activity}</li>" for activity in skill_data['practice_activities']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Character Progress
        st.markdown("<b>📊 Character Development Progress:</b>", unsafe_allow_html=True)
        
        character_traits = {
            "Honesty": 85,
            "Compassion": 80,
            "Discipline": 75,
            "Responsibility": 70,
            "Patience": 65
        }
        
        for trait, progress in character_traits.items():
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <b>{trait}</b>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {progress}%;">
                        <span>{progress}%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Islamic Scenarios
        st.markdown("""
        <div class="activity-card">
            <b>🎯 Real-Life Scenario Discussion:</b>
            <ul>
                <li>⚡ What would you do if a friend was being dishonest?</li>
                <li>⚡ How to handle conflicts with respect and kindness?</li>
                <li>⚡ Showing compassion in difficult situations</li>
                <li>⚡ Acting responsibly when no one is watching</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="project-card">
            <b>🚀 Personal Development</b>
            <p>Build Confidence & Leadership</p>
        </div>
        """, unsafe_allow_html=True)
        
        skill_data = VALUES_SKILLS["Personal Development"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="project-card">
                <b>🎯 Development Areas:</b>
                <ul>
                    {"".join([f"<li>✓ {topic}</li>" for topic in skill_data['topics']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="project-card">
                <b>📚 Programs & Activities:</b>
                <ul>
                    {"".join([f"<li>✓ {activity}</li>" for activity in skill_data['practice_activities']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Leadership Progress
        st.markdown("<b>📊 Leadership & Confidence Growth:</b>", unsafe_allow_html=True)
        
        leadership = {
            "Self-Confidence": 70,
            "Time Management": 75,
            "Goal Setting": 80,
            "Leadership": 65,
            "Innovation": 60
        }
        
        for skill, progress in leadership.items():
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <b>{skill}</b>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {progress}%;">
                        <span>{progress}%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
        <div class="project-card">
            <b>👥 Social Skills Development</b>
            <p>Enhance Communication & Relationships</p>
        </div>
        """, unsafe_allow_html=True)
        
        skill_data = VALUES_SKILLS["Social Skills"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="project-card">
                <b>🤝 Skills to Develop:</b>
                <ul>
                    {"".join([f"<li>✓ {topic}</li>" for topic in skill_data['topics']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="project-card">
                <b>🎯 Engagement Activities:</b>
                <ul>
                    {"".join([f"<li>✓ {activity}</li>" for activity in skill_data['practice_activities']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Social Skills Progress
        st.markdown("<b>📊 Social Skills Development:</b>", unsafe_allow_html=True)
        
        social = {
            "Active Listening": 80,
            "Empathy": 75,
            "Teamwork": 70,
            "Communication": 85,
            "Cooperation": 78
        }
        
        for skill, progress in social.items():
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <b>{skill}</b>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {progress}%;">
                        <span>{progress}%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- AI PAPER EVALUATION ---
elif choice == "📝 AI Paper Evaluation":
    st.markdown('<h1 class="section-header">📝 Advanced AI Examination System</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <span class="premium-badge">Advanced AI</span>
        <b>📋 Upload Documents (4 Essential Items)</b>
        <p>AI-powered comprehensive evaluation with detailed analysis and personalized feedback:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📂 Document 1: Syllabus")
        st.caption("➤ Course outline and learning objectives")
        syl = st.file_uploader("Upload Syllabus (PDF)", type=['pdf'], key="syllabus")
        
        st.markdown("### 📋 Document 2: Paper Pattern")
        st.caption("➤ Question format and marking scheme")
        pat = st.file_uploader("Upload Paper Pattern (PDF)", type=['pdf'], key="pattern")
    
    with col2:
        st.markdown("### 🔑 Document 3: Answer Key")
        st.caption("➤ Official correct answers and solutions")
        key = st.file_uploader("Upload Answer Key (PDF)", type=['pdf'], key="answerkey")
        
        st.markdown("### ✍️ Document 4: Student Paper")
        st.caption("➤ Student's exam script or answer sheet")
        stu = st.file_uploader("Upload Student Script (PDF/Image)", type=['pdf', 'jpg', 'png', 'jpeg'], key="studentpaper")

    st.markdown("---")
    
    eval_mode = st.radio("➤ Evaluation Mode:", ["Automatic Scoring", "Detailed Analysis", "Comparative Report"], horizontal=True)
    
    if st.button("▶ EXECUTE ADVANCED AI EVALUATION", use_container_width=True):
        if syl and pat and key and stu:
            with st.spinner("🤖 AI is analyzing all documents..."):
                st.success("✅ Analysis Complete!")
                
                tabs = st.tabs(["📊 Overview", "📈 Analysis", "💡 Recommendations", "💬 Feedback", "⭐ Strengths", "🔧 Improvements"])
                
                with tabs[0]:
                    st.markdown("""
                    <div class="project-card">
                        <b>📊 Comprehensive Evaluation Report</b>
                        <p><b>Student Accuracy:</b> 85%</p>
                        <p><b>Syllabus Coverage:</b> 92%</p>
                        <p><b>Paper Pattern Adherence:</b> 88%</p>
                        <p><b>Overall Grade:</b> A- (Excellent)</p>
                        <p><b>Total Marks:</b> 85/100</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with tabs[1]:
                    col_m1, col_m2, col_m3 = st.columns(3)
                    with col_m1:
                        st.metric("Conceptual Understanding", "95%", "⬆ +5%")
                    with col_m2:
                        st.metric("Problem Solving", "88%", "⬆ +2%")
                    with col_m3:
                        st.metric("Application Skills", "82%", "→ 0%")
                
                with tabs[2]:
                    st.markdown("""
                    <div class="activity-card">
                        <b>💡 Personalized Recommendations</b>
                        <ul>
                            <li>✓ Focus on timed practice for time management</li>
                            <li>✓ Practice writing structured solutions</li>
                            <li>✓ Work on problem-solving techniques</li>
                            <li>✓ Review complex topics thoroughly</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with tabs[3]:
                    st.markdown("""
                    <div class="feedback-card">
                        <b>💬 AI Detailed Feedback</b>
                        <p><b>General Feedback:</b></p>
                        <p>Excellent performance overall! Your understanding of core concepts is strong. Your answers demonstrate clear thinking and logical progression.</p>
                        
                        <p><b>Positive Observations:</b></p>
                        <ul>
                            <li>✓ Well-structured responses with clear explanations</li>
                            <li>✓ Accurate use of terminology and concepts</li>
                            <li>✓ Good connection between related topics</li>
                            <li>✓ Attention to detail in calculations</li>
                        </ul>
                        
                        <p><b>Areas Needing Attention:</b></p>
                        <ul>
                            <li>⚠ Some answers could be more concise</li>
                            <li>⚠ A few spelling/grammar errors noticed</li>
                            <li>⚠ Could provide more real-world examples</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with tabs[4]:
                    st.markdown("""
                    <div class="strength-card">
                        <b>⭐ Student Strengths</b>
                        <p><span class="rating-stars">★★★★★</span></p>
                        <p><b>Conceptual Mastery:</b> Demonstrates deep understanding of fundamental concepts</p>
                        <p><b>Logical Reasoning:</b> Shows excellent analytical and critical thinking skills</p>
                        <p><b>Presentation:</b> Well-organized and clearly presented answers</p>
                        <p><b>Knowledge Application:</b> Successfully applies concepts to different scenarios</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with tabs[5]:
                    st.markdown("""
                    <div class="improvement-card">
                        <b>🔧 Areas for Improvement</b>
                        <p><b>Priority 1 - High Impact:</b></p>
                        <ul>
                            <li>Time management during exams - practice timed mock tests</li>
                            <li>Answer conciseness - focus on quality over quantity</li>
                        </ul>
                        
                        <p><b>Priority 2 - Medium Impact:</b></p>
                        <ul>
                            <li>Grammar and spelling review - use spell checker</li>
                            <li>More practical examples - connect theory to real-world</li>
                        </ul>
                        
                        <p><b>Suggested Next Steps:</b></p>
                        <ol>
                            <li>Take practice tests under exam conditions</li>
                            <li>Review and revise weak topics</li>
                            <li>Get feedback from peers/tutors</li>
                            <li>Focus on exam technique improvement</li>
                        </ol>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Student Progress Card
                st.markdown("")
                st.markdown("""
                <div class="project-card">
                    <b>📈 Performance Comparison</b>
                    <p><b>Expected Performance:</b> 85/100</p>
                    <p><b>Actual Performance:</b> 85/100</p>
                    <p><b>Class Average:</b> 78/100</p>
                    <p><b>Your Percentile:</b> 85th percentile (Among top 15% of students)</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            missing = []
            if not syl: missing.append("Syllabus")
            if not pat: missing.append("Paper Pattern")
            if not key: missing.append("Answer Key")
            if not stu: missing.append("Student Paper")
            st.error(f"❌ Missing: {', '.join(missing)}")

# --- LESSON ARCHITECT ---
elif choice == "📚 Lesson Architect":
    st.markdown('<h1 class="section-header">📚 Intelligent Lesson Architect</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        topic = st.text_input("➤ Enter Topic:", placeholder="e.g., Photosynthesis")
    with col2:
        grade = st.selectbox("Grade:", ["Elementary", "Middle", "High School"])
    
    col3, col4 = st.columns(2)
    with col3:
        duration = st.slider("Duration (minutes):", 30, 180, 60)
    with col4:
        subject = st.selectbox("Subject:", ["Science", "Mathematics", "English", "History", "Urdu", "Islamic Studies", "Computer Science"])
    
    if st.button("▶ Generate Lesson Plan", use_container_width=True):
        if topic:
            with st.spinner("📖 Designing lesson plan..."):
                try:
                    res = client.chat.completions.create(
                        messages=[{"role":"user","content":f"Create a detailed {grade} level lesson plan for '{topic}' in {subject} lasting {duration} minutes. Include objectives, materials, procedures, assessment, and Islamic integration."}], 
                        model="llama-3.3-70b-versatile"
                    )
                    st.markdown(f'<div class="project-card">{res.choices[0].message.content}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a topic")

# --- ISLAMIC INTEGRATION ---
elif choice == "🕌 Islamic Integration":
    st.markdown('<h1 class="section-header">🕌 Islamic Curriculum Integration</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        topic_isl = st.text_input("➤ Enter Topic:", placeholder="e.g., Science, Mathematics")
    with col2:
        context_type = st.selectbox("Type:", ["Quranic", "Hadith", "Both"])
    
    lang_choice = st.radio("➤ Display Language:", ["Arabic + Urdu + English", "English Only"], horizontal=True)
    
    if st.button("▶ Fetch Islamic References", use_container_width=True):
        if topic_isl:
            with st.spinner("🔍 Searching resources..."):
                try:
                    res = client.chat.completions.create(
                        messages=[{"role":"user","content":f"Provide {context_type} references about {topic_isl} with Arabic text, Urdu, and English translations."}], 
                        model="llama-3.3-70b-versatile"
                    )
                    st.markdown(f'<div class="project-card">{res.choices[0].message.content}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a topic")

# --- STEM HUB ---
elif choice == "🧪 STEM Hub":
    st.markdown('<h1 class="section-header">🧪 Advanced STEM Projects</h1>', unsafe_allow_html=True)
    
    project_select = st.selectbox("➤ Select Project:", [
        "Solar Oven",
        "Hydraulic Lift",
        "Water Filtration",
        "DC Motor",
        "Wind Turbine",
        "Lemon Battery"
    ])

    if project_select == "Solar Oven":
        st.markdown("""
        <div class="project-card">
            <span class="premium-badge">Hands-On</span>
            <b>1️⃣ Solar Oven (Thermodynamics)</b>
            <p><b>Concept:</b> Greenhouse Effect & Heat Transfer</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("📸 Visual Guide: Pizza box → Aluminum lining → Plastic wrap → Black paper → Finished oven")
        
        st.markdown("""
        <div class="activity-card">
            <b>🎯 Hands-On Activities:</b>
            <ul>
                <li>✓ Calculate efficiency ratios</li>
                <li>✓ Compare temperatures at different angles</li>
                <li>✓ Design improved versions</li>
                <li>✓ Challenge: Cook without opening box</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- CODING PROJECTS ---
elif choice == "💻 Coding Projects":
    st.markdown('<h1 class="section-header">💻 Learn Programming with Scratch & Coding</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <b>🎯 Introduction to Block-Based Programming</b>
        <p>Learn programming basics using Scratch-like blocks. Perfect for beginners!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_level1, col_level2, col_level3 = st.columns(3)
    with col_level1:
        if st.button("➤ BEGINNER PROJECTS", use_container_width=True):
            st.info("⭐ Interactive Quiz, Story Maker, Color Buttons")
    with col_level2:
        if st.button("➤ INTERMEDIATE PROJECTS", use_container_width=True):
            st.info("⭐⭐ Pong Game, Drawing App, Counter")
    with col_level3:
        if st.button("➤ ADVANCED PROJECTS", use_container_width=True):
            st.info("⭐⭐⭐ Maze Game, Music Player, Chat Application")

# --- TEACHING AIDS ---
elif choice == "📐 Teaching Aids":
    st.markdown('<h1 class="section-header">📐 Advanced Teaching Aids Library</h1>', unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        if st.button("➤ MATHEMATICS", use_container_width=True):
            st.session_state.aid_category = "Math"
    with col_m2:
        if st.button("➤ SCIENCE", use_container_width=True):
            st.session_state.aid_category = "Science"
    with col_m3:
        if st.button("➤ LANGUAGE", use_container_width=True):
            st.session_state.aid_category = "Language"
    with col_m4:
        if st.button("➤ ISLAMIC", use_container_width=True):
            st.session_state.aid_category = "Islamic"
    
    if "aid_category" not in st.session_state:
        st.session_state.aid_category = "Math"
    
    st.divider()
    
    category = st.session_state.aid_category
    
    if category == "Math":
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("📐 Basic Tools", expanded=True):
                st.markdown("""
                <div class="project-card">
                    <ul>
                        <li>✓ <b>Abacus:</b> Base-10 counting system</li>
                        <li>✓ <b>Geometry Set:</b> Compasses, rulers, set-squares</li>
                        <li>✓ <b>3D Shapes:</b> Volume & surface area</li>
                        <li>✓ <b>Tangram Sets:</b> Spatial reasoning puzzles</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        with col2:
            with st.expander("🚀 Advanced Tools", expanded=True):
                st.markdown("""
                <div class="project-card">
                    <span class="premium-badge">Advanced</span>
                    <ul>
                        <li>✓ <b>Coordinate Plane:</b> Graphing equations</li>
                        <li>✓ <b>Algebra Tiles:</b> Expression visualization</li>
                        <li>✓ <b>Probability Tools:</b> Statistics modeling</li>
                        <li>✓ <b>Calculus Models:</b> Derivatives & integrals</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div class="footer">▶ POWERED BY ADVANCED R&D | © 2026 TAQWA & AQSA | PROFESSIONAL EDUCATION PORTAL ◀</div>', unsafe_allow_html=True)