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
        st.subheader("Data Science Student | Aspiring Analyst")
        st.write("Intern at Cloud Counselage Pvt. Ltd. with a passion for AI and Business Intelligence.")
    
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
    st.title("🚀 Featured Projects")
    
    # Project 1
    with st.expander("🌿 AgroGuard AI (National Tech Event 2026)"):
        st.write("A multi-modal plant pathology system using Deep Learning to diagnose crop diseases.")
        st.button("View Code", key="agro")

    # Project 2
    with st.expander("📧 Email Spam Classification"):
        st.write("Implemented Logistic Regression and Supervised ML to filter spam with high accuracy.")
        st.button("View Code", key="spam")

elif selected == "Experience":
    st.title("💼 Professional Journey")
    st.markdown("### Data Science Intern")
    st.caption("Cloud Counselage Pvt. Ltd. | Aug 2025 - Present")
    st.write("- Developing Power BI dashboards for business insights.")
    st.write("- Building predictive models using Scikit-Learn.")
    st.write("- **Certification:** L&T EduTech A+ in Programming for Data Analytics.")
