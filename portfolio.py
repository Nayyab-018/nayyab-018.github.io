import streamlit as st

st.set_page_config(page_title="Nayyab Faisal | Portfolio", page_icon="🎓", layout="wide")

st.title("Nayyab Faisal")
st.subheader("Aspiring CS, AI & Engineering Undergraduate | IBM Certified in AI, ML & Cybersecurity")
st.write("Building practical Machine Learning, Cybersecurity, and Cyber-Physical Systems from Wah Cantt, Pakistan.")

col1, col2 = st.columns([1, 4])
with col1:
    st.link_button("🚀 Launch Live AI App", "https://streamlit.app", type="primary")
with col2:
    st.link_button("💻 GitHub Profile", "https://github.com")

st.divider()
st.header("Featured Projects")

c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("🛡️ AI Phishing URL Detector")
    st.write("Supervised Random Forest classifier extracting 7 lexical URL signals to detect malicious links in real time.")
    st.link_button("Live Demo", "https://streamlit.app")
    st.link_button("View Code", "https://github.com/AI-Phishing-Detector")

with c2:
    st.subheader("🧠 PyTorch CNN Classifier")
    st.write("Custom Convolutional Neural Network built in PyTorch trained on 70,000 Fashion-MNIST images.")
    st.link_button("View Repository", "https://github.com/PyTorch-CNN-Image-Classifier")

with c3:
    st.subheader("⚽ AI in Soccer Analytics")
    st.write("Sports data analytics and match outcome predictor built with Pandas, Matplotlib, and Scikit-Learn.")
    st.link_button("View Repository", "https://github.com/AI-in-Soccer-Analysis")

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
