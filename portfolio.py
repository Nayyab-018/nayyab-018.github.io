import streamlit as st

st.set_page_config(page_title="Nayyab Faisal | Portfolio", page_icon="🎓", layout="wide")

st.title("Nayyab Faisal")
st.subheader("Aspiring CS, AI & Engineering Undergraduate | IBM Certified in AI, ML & Cybersecurity")
st.write("Building practical Machine Learning, Cybersecurity, and Cyber-Physical Systems from Wah Cantt, Pakistan.")

col1, col2 = st.columns(2)
with col1:
    st.link_button("🚀 Launch Live AI Phishing App", "https://streamlit.app", type="primary")
with col2:
    st.link_button("💻 GitHub Profile", "https://github.com/Nayyab-018")

st.divider()
st.header("Featured Projects")

row1_c1, row1_c2 = st.columns(2)
with row1_c1:
    st.subheader("🛡️ AI Phishing Detector & IoT Alert")
    st.write(
        "Random Forest classifier (97.42% benchmark accuracy on 11,055 URLs) paired with an Arduino Uno "
        "3D alert circuit (Red/Green LEDs + Piezo Buzzer) and a live Streamlit web app."
    )
    st.link_button("Live Demo", "https://streamlit.app")
    st.link_button("View Repository", "https://github.com/Nayyab-018/AI-Phishing-Detector")

with row1_c2:
    st.subheader("🧠 PyTorch CNN Image Classifier")
    st.write(
        "Custom Convolutional Neural Network built from scratch in PyTorch to classify 70,000 "
        "Fashion-MNIST images across 10 apparel categories."
    )
    st.link_button("View Repository", "https://github.com/Nayyab-018/PyTorch-CNN-Image-Classifier")

row2_c1, row2_c2 = st.columns(2)
with row2_c1:
    st.subheader("⚽ AI in Soccer Match Analytics")
    st.write(
        "Zero-dependency trend tracker and Real Madrid ML match predictor built with Pandas, "
        "Matplotlib, and Scikit-Learn using Expected Goals (xG) and rolling metrics."
    )
    st.link_button("View Repository", "https://github.com/Nayyab-018/AI-in-Soccer-Analysis")

with row2_c2:
    st.subheader("🐍 Python Mini-Projects & Automation")
    st.write(
        "Collection of practical Python automation and logic projects, including a Smart Battery Health "
        "Charging Assistant and a Cyber-Vault Security Cracker."
    )
    st.link_button("View Repository", "https://github.com/Nayyab-018/Python-Mini-Projects")

st.divider()
st.header("Academic Excellence (FBISE Islamabad)")
st.info("**Higher Secondary School Certificate (Pre-Engineering):** Grade A1 — 894 / 1100 (81.27%)")
st.info("**Secondary School Certificate (Science Group):** Grade A1 — 1001 / 1100 (91.0%) | **150 / 150 in Computer Science**")

st.header("Verified IBM SkillsBuild Credentials (2026)")
st.markdown("""
- **Getting Started with Generative AI** — IBM SkillsBuild (Credly Verified)
- **Cybersecurity Fundamentals** — IBM SkillsBuild (Credly Verified)
- **Enterprise Design Thinking Practitioner** — IBM SkillsBuild (Credly Verified)
- **Additional Coursework:** Machine Learning & Data Science in IBM watsonx, Foundations of AI, Applying AI, AI in Soccer
""")
