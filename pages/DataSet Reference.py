import streamlit as st

from PIL import Image

st.set_page_config(page_title="About the Lexington Chatbot Team", page_icon="📈")


col1 , col2 = st.columns([9, 1] , gap = "small")

col1.markdown("# Dataset References")

col1.markdown("### Website:")

col1.markdown(
    """
    <p> <a href="https://www.lhsproject.lexingtonma.org/"> Lexington High School (LHS) Building Project website </a> </p>   
    <p><a href="https://www.lhsproject.lexingtonma.org/projectfaqs/"> Project FAQs on the LHS Building Project website </a> </p>
    <p><a href="https://www.lhsproject.lexingtonma.org/community-submissions"> Staged/phased plans will cost more than Bloom </a>  </p>
    <p><a href="https://www.yes4lex.org/cec-report"> Capital Expenditures Committee and Appropriation Committee Reports on Article 8 (Nov. 6, 2024)</a> </p>
    <p><a href="https://lexobserver.org/2024/10/17/inside-the-the-hot-stuffy-overcrowded-lexington-high-school/">Inside the the hot, stuffy, overcrowded, Lexington High School (Oct. 17, 2024) </a></p>
    <p><a href="https://lexobserver.org/2024/10/16/lexington-high-school-is-old-and-run-down-here-are-some-photos-that-show-it/">Lexington High School is old and run down (Oct. 16, 2024) </a></p>
    <p><a href="https://lexobserver.org/2024/10/17/how-years-of-construction-at-lhs-will-affect-its-students/">How years of construction at LHS will affect its students (Oct. 17, 2024) </a></p>
    <p><a href="https://lexobserver.org/2024/10/18/what-sustainability-features-are-in-the-works-for-the-new-high-school-building-and-are-they-worth-the-cost/">What sustainability features are in the works for the new high school building, and are they worth the cost? (Oct. 18, 2024)</a></p>
    <p><a href="https://lexobserver.org/2024/10/09/letter-to-the-editor-a-new-high-school-to-meet-the-educational-needs-of-future-generations/">A new high school to meet the educational needs of future generations (Oct. 9, 2024) </a></p>
    <p><a href="https://www.yes4lex.org/march-2025-newsletter">Yes for Lexington March 25, 2025 - March Newsletter </a></p>
    <p><a href="https://www.yes4lex.org/2025-02-26-newsletter">Yes for Lexington Feb. 26, 2025 - 2025 Town Election Edition </a></p>
    <p><a href="https://lexobserver.org/category/lhs-watch/">The Lexington Observer LHS Watch -  Reporting on the LHS Building Project </a></p>
    <p><a href="https://lexobserver.org/2024/10/17/explaining-the-six-concepts-for-the-new-lhs-and-which-are-front-runners/">Explaining the six concepts for the new LHS, and which are front-runners (Oct. 17, 2024) </a></p>

     """,
    unsafe_allow_html=True
)

col1.markdown("### Google Docs:")

col1.markdown(
    """
   <p> <a href="https://docs.google.com/document/d/1HVlamMRpUJJe_0vHDfoYTuwLw1Fx54CYeB1jF6YOaz4/edit?tab=t.0"> "Bloom" is the right size for anticipated enrollment </a> </p>   
   <p> <a href="https://docs.google.com/document/d/1DX94RbuXva7kAFmrtk35jKwLwBuLy7dGRNNmcSFTpEY/edit?tab=t.0"> Staged/phased plans cost $300 million MORE than Bloom </a> </p>   

    """,
    unsafe_allow_html=True
)

col1.markdown("### Google Slide:")
col1.markdown(
    """
  <p> <a href="https://docs.google.com/presentation/d/1vhpH_ouaOfkL0nzV--iJrqisoDovI93p/edit?slide=id.p1#slide=id.p1"> Comparing LHS project costs to other high school project costs - Dore + Whittier (Aug. 12, 2024) </a> </p>   

    """,
    unsafe_allow_html=True
)

col1.markdown("### PDFs")

col1.markdown(
    """
    <p> <a href="https://drive.google.com/file/d/1Uzuo95T6bT_O2aZUWbx6UQ4hooY3VaM3/view"> MSBA Facilities Assessment Subcommittee Presentation (Jan. 15, 2025) </a> </p> 
    <p> <a href="https://www.lexingtonma.gov/DocumentCenter/View/12971/Article-1-School-Building-Committee-Report-Presentation?bidId="> Update for Town Meeting (presentation) (Nov. 13, 2024) </a> </p>   
    <p> <a href="https://www.lexingtonma.gov/DocumentCenter/View/12970/School-Building-Committee-Report-STM-2024-1?bidId="> Report to Town Meeting (Nov. 13, 2024) </a> </p>  
    <p> <a href="https://drive.google.com/file/d/1rZMpagsQ2Nbuy5N1kubjoj27jzTV2iGT/view"> formal endorsement of the “Bloom” option (Oct. 20, 2024) </a> </p>  
    <p> <a href="https://static1.squarespace.com/static/63125a2b89187e01574a9f7e/t/67e182bae094a35cb40162a5/1742832314945/Tax+payer+project+impact+slide+18+Jan+2025+presentation.pdf"> Town Finance staff continue to model projected impact on taxpayers </a> </p>  
    <p> <a href="https://drive.google.com/file/d/1_nL29hwzaIPXU098jJJE392rqFvyWcXT/view"> "Thrive" costs $860 million, requires Art. 97 land swap, and not ready until 2035 </a> </p>  
    <p> <a href="https://drive.google.com/file/d/13MSjN8bVjN0syHtJJ_JyBGe2QNoKZ71R/view"> Latest cost comparison of the six options (Oct. 16, 2024) </a> </p>  
    <p> <a href="https://static1.squarespace.com/static/63125a2b89187e01574a9f7e/t/66f04b4fccadcf227a90f6d6/1727023961349/%28USE%29+Community+Forum+%237+Sustainbility+One+Sheet.pdf"> Economics of Designing Net Zero Schools (Sept. 10, 2024) </a> </p>    

    """,
    unsafe_allow_html=True
)

col1.markdown("### Video mp4")

col1.markdown(
    """
   <p> <a href="https://drive.google.com/file/d/1SR1GG5yh6VZsDyTOYh80JBfONJXxnwSF/view"> Explaining the latest cost estimates - Dore + Whittier (Oct. 10, 2024) </a> </p>  
 
    """,
    unsafe_allow_html=True
)

col1.markdown("### Video on YouTube")

col1.markdown(
    """

    <p> <a href="https://www.youtube.com/watch?v=xy-MoQU7dpc"> Tour of Waltham High School and LHS (Oct. 4, 2024) </a> </p>  
    <p> <a href="https://www.youtube.com/watch?v=mdMmunQNP98"> Lexington Local Episode - Yes4Lex ft. Taylor Singh (Sept. 26, 2024) </a> </p>  

 
    """,
    unsafe_allow_html=True
)




