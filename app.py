import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

# Page Config
st.set_page_config(page_title="Nishtha Dighe | Portfolio", layout="wide")

# Load CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📌 Contact")
    st.write("📍 Kalyan, Maharashtra")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/nishtha-dighe-370114325)")
    st.markdown("[GitHub](https://github.com/nishthadighe-bit)")
    st.info("SGPI: ~9.28 (SY Data Science)")
    
    st.write("---")
    # Resume Download Section
    try:
        with open("NISHTHA DIGHE CV (1).pdf", "rb") as f:
            st.download_button("📄 Download My Resume", f, "Nishtha_Dighe_CV.pdf")
    except:
        st.error("Resume file not found")

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Experience"],
    icons=["house", "code-slash", "briefcase"],
    orientation="horizontal",
    styles={"container": {"background-color": "#121212"}}
)

if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Hi, I'm Nishtha Dighe")
        st.subheader("Data Science Student | AI Enthusiast")
        st.write("Data Science Intern at Cloud Counselage Pvt. Ltd. focused on Machine Learning and BI Dashboards.")
    
    st.write("---")
    st.subheader("🌌 My Skill Universe (Interactive 3D)")
    skills_df = pd.DataFrame({
        'Skill': ['Python', 'SQL', 'ML', 'Power BI', 'Deep Learning', 'R'],
        'Level': [95, 85, 90, 95, 80, 75],
        'Category': ['Language', 'Data', 'AI', 'BI', 'AI', 'Language']
    })
    fig = px.scatter_3d(skills_df, x='Skill', y='Level', z='Level', color='Category', 
                        title="Rotate to Explore Skills", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Projects":
    st.title("🚀 Project Showcase")

    # Section 1: Power BI Dashboards
    st.markdown("### 📊 Power BI Dashboards")
    c1, c2 = st.columns(2)
    with c1:
        st.image("dashboard_academic.png", caption="Student Economic & Academic Insights")
    with c2:
        st.image("dashboard_trade.png", caption="Global Trade & Trade Balance Analysis")

    st.write("---")

    # Section 2: AI & Machine Learning
    st.markdown("### 🧠 AI & Deep Learning Applications")
    
    with st.expander("🌿 AgroGuard: Intelligent Plant Pathology"):
        st.image("agroguard_ss.png")
        st.write("Selected for National Level Tech Presentation. Diagnoses plant diseases using CNNs.")
        st.link_button("View Code", "https://github.com/nishthadighe-bit")

    with st.expander("👗 Fashion MNIST Classifier"):
        st.image("fashion_ss.png")
        st.write("A computer vision tool that classifies apparel using Deep Learning.")
        st.link_button("View Code", "https://github.com/nishthadighe-bit")

elif selected == "Experience":
    st.title("💼 Professional & Academic Journey")
    
    st.markdown("### Data Science Intern")
    st.caption("Cloud Counselage Pvt. Ltd. | 2025 - Present")
    st.write("- Developing interactive Power BI dashboards for market analysis.")
    st.write("- Implementing predictive models using Scikit-Learn.")

    st.write("---")
    st.markdown("### 🏅 Certifications")
    
    # Python Certification
    with st.expander("L&T EduTech: Programming For Data Analytics (A+ Grade)"):
        with open("NISHTHA SANDESH DIGHE_Programming For Data Analytics (Python)  (2).pdf", "rb") as f:
            st.download_button("View Certificate", f, "Python_Cert.pdf", key="cert1")

    # Fundamentals Certification
    with st.expander("L&T EduTech: Fundamentals of Data Science"):
        with open("NISHTHA SANDESH DIGHE_Fundamentals Of Data Science.pdf", "rb") as f:
            st.download_button("View Certificate", f, "Fundamentals_Cert.pdf", key="cert2")
