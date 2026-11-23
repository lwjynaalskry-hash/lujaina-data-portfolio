import streamlit as st
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Lujaina Elaskary | Portfolio",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# EDIT THESE LINKS BEFORE PUBLISHING
# =========================================================
LINKEDIN_URL = "https://www.linkedin.com/"  # Replace with your profile URL
GITHUB_URL = "https://github.com/"          # Replace with your profile URL
EMAIL_ADDRESS = ""                          # Example: name@example.com

# Optional: put your CV PDF in the same folder as app.py
CV_PATH = Path(__file__).parent / "Lujaina_CV.pdf"

# =========================================================
# CUSTOM CSS — animated aurora + stars + responsive cards
# =========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #080b18;
        --panel: rgba(21, 26, 48, 0.88);
        --purple: #c3a2ff;
        --blue: #aebeff;
        --text: #eeeaf8;
        --muted: #c9c5dc;
        --border: rgba(174, 137, 255, 0.34);
    }

    html { scroll-behavior: smooth; }

    * { font-family: 'Inter', sans-serif; }

    .stApp {
        background:
            radial-gradient(circle at 12% 18%, rgba(111, 67, 180, .18), transparent 28%),
            radial-gradient(circle at 85% 30%, rgba(58, 91, 190, .16), transparent 30%),
            var(--bg);
        color: var(--text);
        overflow-x: hidden;
    }

    /* Moving aurora layer */
    .stApp::before {
        content: "";
        position: fixed;
        inset: -35%;
        z-index: 0;
        pointer-events: none;
        background:
            radial-gradient(ellipse at 25% 35%, rgba(137, 77, 220, .25), transparent 34%),
            radial-gradient(ellipse at 75% 25%, rgba(65, 105, 230, .20), transparent 32%),
            radial-gradient(ellipse at 55% 78%, rgba(166, 91, 255, .18), transparent 35%);
        filter: blur(24px);
        animation: auroraMove 18s ease-in-out infinite alternate;
    }

    /* Star field */
    .stApp::after {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        opacity: .45;
        background-image:
            radial-gradient(2px 2px at 8% 18%, #ffffff 50%, transparent 65%),
            radial-gradient(2px 2px at 24% 72%, #c5a4ff 50%, transparent 65%),
            radial-gradient(2px 2px at 43% 32%, #ffffff 50%, transparent 65%),
            radial-gradient(2px 2px at 67% 16%, #aebeff 50%, transparent 65%),
            radial-gradient(2px 2px at 82% 66%, #ffffff 50%, transparent 65%),
            radial-gradient(2px 2px at 93% 35%, #c5a4ff 50%, transparent 65%);
        background-size: 390px 390px;
        animation: starDrift 34s linear infinite;
    }

    @keyframes auroraMove {
        0%   { transform: translate3d(-2%, -1%, 0) scale(1); }
        50%  { transform: translate3d(3%, 2%, 0) scale(1.08); }
        100% { transform: translate3d(-1%, 4%, 0) scale(1.03); }
    }

    @keyframes starDrift {
        from { background-position: 0 0; }
        to   { background-position: 390px 390px; }
    }

    /* Keep Streamlit content above the animated background */
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"] {
        background: transparent !important;
    }

    .block-container {
        max-width: 1180px;
        padding: 1.8rem 2rem 3.5rem;
        position: relative;
        z-index: 1;
    }

    #MainMenu, footer, header { visibility: hidden; }

    /* Navigation */
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 18px;
        padding: 18px 25px;
        margin-bottom: 58px;
        border: 1px solid var(--border);
        border-radius: 20px;
        background: rgba(17, 21, 40, .82);
        backdrop-filter: blur(14px);
        box-shadow: 0 10px 35px rgba(0, 0, 0, .16);
    }

    .logo {
        color: var(--purple);
        font-size: 27px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .nav-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 22px;
    }

    .nav-links a {
        color: #ddd8ef !important;
        text-decoration: none !important;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: color .25s ease;
    }

    .nav-links a:hover { color: var(--purple) !important; }

    /* Hero */
    .hero {
        position: relative;
        overflow: hidden;
        text-align: center;
        padding: 92px 28px 86px;
        border: 1px solid rgba(177, 132, 255, .55);
        border-radius: 34px;
        background:
            radial-gradient(ellipse at 50% 5%, rgba(132, 82, 205, .24), transparent 62%),
            linear-gradient(145deg, rgba(28, 29, 59, .92), rgba(13, 17, 35, .91));
        box-shadow: 0 0 45px rgba(142, 91, 220, .13);
        animation: heroPulse 5s ease-in-out infinite alternate;
    }

    .hero::before {
        content: "";
        position: absolute;
        width: 280px;
        height: 280px;
        top: -180px;
        right: -80px;
        border-radius: 50%;
        background: rgba(170, 125, 255, .18);
        filter: blur(35px);
    }

    @keyframes heroPulse {
        from { box-shadow: 0 0 22px rgba(142, 91, 220, .12); }
        to   { box-shadow: 0 0 52px rgba(142, 91, 220, .28); }
    }

    .hero-tag {
        display: inline-block;
        padding: 11px 23px;
        border: 1px solid rgba(190, 151, 255, .65);
        border-radius: 50px;
        background: rgba(80, 53, 119, .42);
        color: #dfccff;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1px;
    }

    .hero h1 {
        margin: 30px 0 14px;
        color: var(--purple);
        font-size: clamp(36px, 6vw, 72px);
        line-height: 1.12;
        font-weight: 800;
        letter-spacing: -2px;
        overflow-wrap: anywhere;
        text-shadow: 0 0 32px rgba(172, 126, 255, .35);
    }

    .hero h2 {
        margin: 0;
        color: var(--blue);
        font-size: clamp(20px, 3vw, 30px);
        font-weight: 700;
    }

    .hero-line {
        width: min(560px, 90%);
        margin: 26px auto 0;
        color: #e0dced;
        font-size: 17px;
        line-height: 1.8;
        overflow: hidden;
        white-space: normal;
    }

    .hero-caption {
        margin: 12px 0 0;
        color: var(--muted);
        font-size: 14px;
    }

    /* Section headings and cards */
    .section-title {
        margin: 76px 0 25px;
        color: var(--purple);
        font-size: clamp(25px, 3vw, 34px);
        font-weight: 800;
        letter-spacing: -.7px;
    }

    .about-card, .skill-card, .project-card, .timeline-card, .cert-card, .contact-card {
        border: 1px solid var(--border);
        border-radius: 20px;
        background: var(--panel);
        backdrop-filter: blur(10px);
        box-shadow: 0 12px 32px rgba(0, 0, 0, .12);
    }

    .about-card {
        padding: 30px 32px;
        color: #e0dced;
        font-size: 15px;
        line-height: 2;
    }

    .skill-card {
        min-height: 205px;
        padding: 24px;
        margin-bottom: 14px;
        transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
    }

    .skill-card:hover, .project-card:hover {
        transform: translateY(-6px);
        border-color: rgba(195, 162, 255, .85);
        box-shadow: 0 14px 35px rgba(128, 82, 194, .20);
    }

    .skill-card h3, .project-card h3, .timeline-card h3, .cert-card h3 {
        margin-top: 0;
        color: var(--purple);
        font-size: 18px;
        font-weight: 700;
    }

    .skill-card p, .project-card p, .timeline-card p, .cert-card p {
        margin-bottom: 0;
        color: #d4d0e4;
        font-size: 14px;
        line-height: 1.9;
    }

    .project-card {
        min-height: 225px;
        padding: 25px;
        margin-bottom: 16px;
        transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
    }

    .project-tech {
        margin-top: 17px;
        color: var(--blue);
        font-size: 12px;
        font-weight: 600;
        line-height: 1.8;
    }

    .timeline-card {
        padding: 23px 25px;
        margin: 15px 0;
        border-left: 3px solid #a77aff;
        border-radius: 5px 18px 18px 5px;
    }

    .cert-card {
        padding: 23px;
        min-height: 120px;
        margin-bottom: 14px;
    }

    .contact-card {
        padding: 42px 22px;
        text-align: center;
        background: linear-gradient(135deg, rgba(43, 32, 75, .92), rgba(19, 25, 48, .94));
    }

    .contact-card h2 {
        color: var(--purple);
        font-size: 25px;
    }

    .contact-card p {
        color: #ddd8ef;
        line-height: 1.8;
    }

    .footer {
        padding: 38px 10px 8px;
        color: #9692ad;
        text-align: center;
        font-size: 12px;
        line-height: 1.8;
    }

    /* Streamlit buttons */
    .stLinkButton a, .stDownloadButton button {
        border: 1px solid #a77aff !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #7650ad, #59418d) !important;
        color: white !important;
        font-weight: 600 !important;
        transition: .25s ease !important;
    }

    .stLinkButton a:hover, .stDownloadButton button:hover {
        border-color: #d0b5ff !important;
        box-shadow: 0 0 22px rgba(167, 122, 255, .30) !important;
        transform: translateY(-2px);
    }

    @media (max-width: 720px) {
        .block-container { padding: 1rem 1rem 2.5rem; }
        .navbar { justify-content: center; margin-bottom: 32px; padding: 17px; }
        .nav-links { justify-content: center; gap: 13px; }
        .nav-links a { font-size: 11px; }
        .hero { padding: 65px 17px; border-radius: 25px; }
        .hero h1 { letter-spacing: -1px; }
        .about-card { padding: 22px; }
        .section-title { margin-top: 55px; }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: .01ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
            transition-duration: .01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGATION
# =========================================================
st.markdown(
    """
    <div class="navbar">
        <div class="logo">LE.</div>
        <nav class="nav-links">
            <a href="#home">HOME</a>
            <a href="#about">ABOUT</a>
            <a href="#skills">SKILLS</a>
            <a href="#projects">PROJECTS</a>
            <a href="#education">EDUCATION</a>
            <a href="#certifications">CERTIFICATES</a>
            <a href="#contact">CONTACT</a>
        </nav>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HOME
# =========================================================
st.markdown(
    """
    <div id="home"></div>
    <section class="hero">
        <div class="hero-tag">✦ WELCOME TO MY DIGITAL PORTFOLIO ✦</div>
        <h1>LUJAINA ELASKARY</h1>
        <h2>Data Engineer | Data Analyst</h2>
        <div class="hero-line">Turning Raw Data Into Meaningful Insights</div>
        <p class="hero-caption">Passionate about Data, Technology and Building Smart Solutions.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

with open("Lujaina Elaskary_CV.pdf", "rb") as pdf:
    st.download_button(
        label="📄 Download My CV",
        data=pdf,
        file_name="Lujaina_Elaskary_CV.pdf",
        mime="application/pdf"
    )
# =========================================================
# ABOUT
# =========================================================
st.markdown('<div id="about"></div><div class="section-title">01. About Me</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="about-card">
        I am a Computer Science student at Alexandria University, interested in
        Data Engineering, Data Analytics, and Artificial Intelligence.
        <br><br>
        I enjoy transforming raw data into meaningful insights, designing
        data-driven solutions, and exploring technologies that help solve
        real-world problems.
        <br><br>
        I am continuously developing my technical skills through academic
        projects, practical training, and collaborative work. I am always
        looking for opportunities to learn, contribute, and grow.
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# SKILLS
# =========================================================
st.markdown('<div id="skills"></div><div class="section-title">02. Technical Skills</div>', unsafe_allow_html=True)

skill_columns = st.columns(3)
skills = [
    ("💻 Programming", "Python<br>SQL<br>Java<br>C++"),
    ("📊 Data & Analytics", "Pandas & NumPy<br>Data Cleaning<br>Data Visualization<br>R & Machine Learning fundamentals"),
    ("⚙️ Tools & Technologies", "Power BI<br>Streamlit<br>Git & GitHub<br>Azure fundamentals"),
]
for column, (heading, items) in zip(skill_columns, skills):
    with column:
        st.markdown(
            f'<div class="skill-card"><h3>{heading}</h3><p>{items}</p></div>',
            unsafe_allow_html=True,
        )

# =========================================================
# PROJECTS
# =========================================================
st.markdown('<div id="projects"></div><div class="section-title">03. Featured Projects</div>', unsafe_allow_html=True)

projects = [
    (
        "🚚 Food Delivery Analysis & Prediction",
        "Analyzed food delivery data, explored service performance, applied clustering and decision-tree modeling, and presented insights through an interactive dashboard.",
        "R · K-Means · Decision Trees · R Shiny",
    ),
    (
        "🚑 Emergency Vehicle Routing System",
        "Built a pathfinding application that finds efficient routes for emergency vehicles while considering blocked cells and incident locations.",
        "Python · A* Search · Tkinter",
    ),
    (
        "🏥 Hospital Appointment Management System",
        "Developed a Java application to organize hospital appointments and support basic management operations.",
        "Java · Object-Oriented Programming",
    ),
    (
        "📦 Data Structures Projects",
        "Implemented practical data-structure concepts through linked lists, stacks, queues, doubly linked lists, and an LRU cache.",
        "Java · Linked Lists · Stack · Queue · LRU Cache",
    ),
]

for start in range(0, len(projects), 2):
    cols = st.columns(2)
    for col, project in zip(cols, projects[start:start + 2]):
        title, description, technologies = project
        with col:
            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{title}</h3>
                    <p>{description}</p>
                    <div class="project-tech">{technologies}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# =========================================================
# EDUCATION & EXPERIENCE
# =========================================================
st.markdown('<div id="education"></div><div class="section-title">04. Education & Experience</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="timeline-card">
        <h3>🎓 Alexandria University</h3>
        <p>Faculty of Computers and Information · Computer Science</p>
    </div>
    <div class="timeline-card">
        <h3>🚀 Digital Egypt Pioneers Initiative (DEPI)</h3>
        <p>Round 5 · Data Analytics Track · Technical training and practical projects</p>
    </div>
    <div class="timeline-card">
        <h3>💼 CIB Summer Internship</h3>
        <p>Generative AI training</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# CERTIFICATIONS
# =========================================================
st.markdown('<div id="certifications"></div><div class="section-title">05. Certifications</div>', unsafe_allow_html=True)

cert_columns = st.columns(2)
certificates = [
    ("🏅 CIB Summer Internship", "Generative AI"),
    ("🏅 AI Literacy", "MCIT · Empower Yourself"),
    ("🏅 Database Fundamentals", "Mahara-Tech"),
    ("🏅 Digital Egypt Pioneers Initiative", "DEPI · Round 5 · Data Analytics"),
]
for column, (heading, detail) in zip(cert_columns * 2, certificates):
    with column:
        st.markdown(
            f'<div class="cert-card"><h3>{heading}</h3><p>{detail}</p></div>',
            unsafe_allow_html=True,
        )


# =========================================================
# CONTACT
# =========================================================

st.markdown(
    '<div id="contact"></div>'
    '<div class="section-title">06. Let\'s Connect</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="contact-card">
    <h2>Have an idea or opportunity?</h2>
    <p>
        I would love to connect, collaborate,
        and build something meaningful.
    </p>
    <p>Let's create something amazing together! ✨</p>
</div>
""", unsafe_allow_html=True)

# Contact Buttons
button_columns = st.columns(3)

with button_columns[0]:
    st.link_button(
        "LinkedIn ↗",
        LINKEDIN_URL,
        use_container_width=True
    )

with button_columns[1]:
    st.link_button(
        "GitHub ↗",
        GITHUB_URL,
        use_container_width=True
    )

with button_columns[2]:
    st.link_button(
        "📧 Email Me",
        "mailto:lwjynaalskry@gmail.com",
        use_container_width=True
    )

# Footer
st.markdown("""
<div class="footer">
    <p>Designed & Built with 💜 by Lujaina Elaskary</p>
    <p>© 2026 All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# CV DOWNLOAD (optional)
# =========================================================
if CV_PATH.exists():
    st.write("")
    with open(CV_PATH, "rb") as cv_file:
        st.download_button(
            label="📄 Download My CV",
            data=cv_file,
            file_name="Lujaina_Elaskary_CV.pdf",
            mime="application/pdf",
        )

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        Designed & Built with 💜 by Lujaina Elaskary<br>
        © 2026 All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True,
)
