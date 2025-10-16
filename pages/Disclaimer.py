import streamlit as st

from PIL import Image

st.set_page_config(page_title="About the Lexington Chatbot Team", page_icon="📈")


col1 , col2 = st.columns([9, 1] , gap = "small")

col1.markdown("# Disclaimer")

 

col1.markdown(
    """
    <p>
    
This chatbot uses a RAG + ReAct + LLM architecture to search, retrieve, and summarize information from official government documents. While we strive for accuracy, the responses may contain mistakes, omissions, or outdated information.

Please always verify the information by reading the original government documents linked in each response. The chatbot is an assistive tool and does not provide legal, regulatory, or official advice. Final interpretation and verification are the responsibility of the user.
    """,
    unsafe_allow_html=True
)
 

 

    
 

