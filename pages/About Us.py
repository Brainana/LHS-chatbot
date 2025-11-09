import streamlit as st

from PIL import Image

st.set_page_config(page_title="About the Lexington Chatbot Team", page_icon="📈")


col1 , col2 = st.columns([9, 1] , gap = "small")

col1.markdown("# Lexington Chatbot Team")

col1.markdown("### Our Mission:")

col1.markdown(
    """
    <p>
    The LHS Chatbot is specially built to answer questions about the new Lexington High School Project. 
    It saves residents' time by summarizing thousands of pages of official project documents, offering quick, clear answers with links to sources for user verification. 
    While the chatbot is neutral in position, it can answer questions about costs, timelines, tax impact, and more. 
    With this project, we hope to help residents better understand this important and widely discussed topic, enabling them to make well-informed decisions ahead of the LHS Project Special Debt Exclusion Vote on December 8th.
    </p>
    <p>
    Our chatbot has also been featured in <a href="https://lexobserver.org/2025/10/01/lexington-high-school-building-project-chatbot/" target="_blank">The Lexington Observer</a>!
    </p>
    <p>
    We offer multilingual support, so you can interact with the chatbot in your preferred language. 
    If you have any questions or suggestions, please feel free to email us at <a href="mailto:lyst.connect@gmail.com">lyst.connect@gmail.com</a>.
    </p>
    """,
    unsafe_allow_html=True
)
col1.write("")

col1_sub, col2_sub = col1.columns(2)


with col1_sub:
    col1_sub.markdown("### Team Members:")

    col1_sub.write("Jerry Xu (Project Lead)")
    col1_sub.write("Justin Wang (Developer)")
    col1_sub.write("Jasmine Gu (Developer)")
    col1_sub.write("Joley Leung (Graphics)")

with col2_sub:
    col2_sub.markdown("### Mentors:")

    col2_sub.write("Wei Ding")
    col2_sub.write("Jeannie Lu")


    

col2.markdown('<a href="https://lexyouthstem.org/" target="_blank"><img src="https://brainana.github.io/LexBudgetDocs/images/teamlogo.png" width="200"></a>', unsafe_allow_html=True)





