import streamlit as st

from PIL import Image

st.set_page_config(page_title="About the Lexington Chatbot Team", page_icon="📈")


col1 , col2 = st.columns([9, 1] , gap = "small")

col1.markdown("# Dataset References")

col1.markdown("### Chatbot Dataset:")

col1.markdown(
    """
    The Chatbot relies on the following authoritative resources to deliver reliable information to users about the LHS Building Project and related community developments:
    <p>  Official documents from the LHS Building Project teams </p> 
    <p> <a href="https://docs.google.com/document/d/1NWFWo2WmQ3kVV-Ty1cXBTPt3cOa5viWzXxEvZnT0TT0/edit?tab=t.0"> LHS Official Documents - Google Docs </a> </p> 

    <p>  LHS building project meeting presentations </p> 
    <p> <a href="https://docs.google.com/document/d/1qRCKL0NOaVWwjHbeTutIGZtWAz4Mv09tmLgfhXR3t3Q/edit?tab=t.0"> Summary of School Building Committee Meetings - Google Docs </a> </p> 

    <p>  Preferred Schematic Report (PSR) Submission  </p> 
    <p> <a href="https://drive.google.com/drive/folders/1UasC2_q4gXGHajgIUA7vQPsbFy9NBq56"> PSR Submission - Google Drive </a> </p> 

    <p>  Preliminary Design Program Submission </p> 
    <p> <a href="https://www.lhsproject.lexingtonma.org/pdp"> https://www.lhsproject.lexingtonma.org/pdp </a> </p> 
 
    <p>  Public Schematic Design (SD) Submission </p> 
    <p> <a href="https://drive.google.com/drive/folders/10zlwl4LyQaNl-umkFRgwJ9fLTVa9UwJB"> Public SD Submission - Google Drive </a> </p> 
    
       
    Website documents from verified sources

     """,
    unsafe_allow_html=True
)



col1.markdown("### Chatbot Most Recent Datasets Inclusion:")

col1.markdown(
    """
    <p>  1.       Community Submission Page: </p> 
    <p> <a href="https://www.lhsproject.lexingtonma.org/community-submissions"> Community Submissions — Lexington High School Building Project </a> </p>  
    <p>  2.      Senior Tax Deferral Program: </p> 
    <p> <a href="https://www.lexingtonma.gov/169/Senior-Tax-Deferral-Program"> https://www.lexingtonma.gov/169/Senior-Tax-Deferral-Program </a> </p>
    <p>  3.       Lexington High School Project Tax Impact Calculator: </p> 
    <p> <a href="https://www.lexingtonma.gov/2431/Lexington-High-School-Project-Tax-Impact"> Lexington High School Project Tax Impact Calculator | Lexington, MA </a> </p>  
    <p> 4.       Memo from Dr. Julie Hacket: </p> 
    <p> <a href="https://docs.google.com/document/d/1HW5rzzlmkPLNnzrkFgf2WnpuSJ3JVOLe6r2cq2sd53s/edit?tab=t.0#heading=h.jgp2aw1tpptm"> 2025-01-24 Enrollment & Housing Update - Google Docs </a> </p>
    <p> <a href="https://docs.google.com/document/d/1HVlamMRpUJJe_0vHDfoYTuwLw1Fx54CYeB1jF6YOaz4/edit?tab=t.0"> Bloom Design & Known Housing Development_01-29-2025 - Google Docs </a> </p>
 
    <p> 5.     Enrolment Data: </p> 
    <p> <a href="https://profiles.doe.mass.edu/profiles/student.aspx?orgcode=01550505&orgtypecode=6"> Enrollment Data (2024-25) - Lexington High (01550505) </a> </p>  
    <p> 6.     Lasted LHS Building Project Presentation </p> 
    <p> <a href="https://docs.google.com/document/d/1qRCKL0NOaVWwjHbeTutIGZtWAz4Mv09tmLgfhXR3t3Q/edit?tab=t.0"> Summary of School Building Committee Meetings - Google Docs </a>  (Latest Doc included is the Oct 6th SBC Meeting No. 35 Meeting Presentation)  </p>

    """,
    unsafe_allow_html=True
)


col1.markdown("### Project Funding:")
col1.markdown(

    """
    <p> The Chatbot is a community service project led by Lexington High School students and mentored by Dr. Ding Wei and Jeannie Lu. Its infrastructure is hosted on Amazon Web Services (AWS), utilizing EC2 and DynamoDB. The project is currently partially funded by the Amazon Web Services Credit Program for Smaller Nonprofits. </p> 
    <p>  To learn more about the project, please visit our <a href="https://youthsteaminitiative.org/lexbudget.html">project page</a> on the Youth STEAM Initiative website.  Community donations are welcome and can be made through the Youth STEAM Initiative’s<a href=" https://youthsteaminitiative.org/donate.html"> donation site.</a>  This collective support ensures the ongoing development and accessibility of the Chatbot as a resource for Lexington residents.
</p>   

    """,
    unsafe_allow_html=True
)