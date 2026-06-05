import streamlit as st

st.set_page_config(
    page_title="Ronak Singhania | Landing Page",
    page_icon="👋",
    layout="wide"
)

# Hero Section
st.title("👋 Hello World, I’m Ronak Singhania")

st.subheader(
    "PhD Scholar | Consumer Behavior Researcher | Strategy & Analytics Thinker"
)

st.write(
    """
    Welcome to my first Streamlit landing page.  
    I am Ronak Singhania, a PhD scholar at IIM Indore, working in the area of
    consumer behavior, judgment under uncertainty, fairness, entitlement, and decision-making.
    """
)

st.divider()

# About Me
col1, col2 = st.columns(2)

with col1:
    st.header("About Me")
    st.write(
        """
        I enjoy working at the intersection of research, strategy, data, and human psychology.
        My academic work focuses on understanding how people make decisions, especially when
        effort, luck, fairness, and rewards interact.
        """
    )

    st.write(
        """
        Beyond research, I like building structured systems — whether for academic ideas,
        personal finance, stock analysis, cricket simulations, or everyday decision-making.
        """
    )

with col2:
    st.header("Current Focus")
    st.markdown(
        """
        - 🎓 PhD in Marketing at **IIM Indore**
        - 🧠 Research on **entitlement, luck, fairness, and consumer judgment**
        - 📊 Interested in **data-backed decision systems**
        - 🏏 Deep interest in **cricket strategy and leadership**
        - 🏠 Currently building life in **Hyderabad**
        """
    )

st.divider()

# Research Section
st.header("My Research Interests")

st.markdown(
    """
    My research explores how people interpret effort, eligibility, chance, and fairness.
    Some of my key themes include:
    """
)

research_cols = st.columns(3)

with research_cols[0]:
    st.metric("Theme 1", "Effort")
    st.write("How effort changes expectations, entitlement, and perceived deservingness.")

with research_cols[1]:
    st.metric("Theme 2", "Luck")
    st.write("How people misread chance-based outcomes through personal narratives.")

with research_cols[2]:
    st.metric("Theme 3", "Fairness")
    st.write("How consumers judge rewards, thresholds, and eligibility rules.")

st.divider()

# Personality / Style
st.header("How I Think")

st.write(
    """
    I like breaking complex things into structured frameworks.  
    I enjoy asking: What is really happening underneath the surface?  
    Whether it is a research problem, a financial decision, a cricket strategy,
    or a character analysis, I naturally look for systems, motives, trade-offs,
    and hidden patterns.
    """
)

st.info(
    "This landing page is built with Streamlit — a simple Python framework for creating interactive web apps."
)

# Footer
st.divider()

st.caption("Built with ❤️ using Streamlit")