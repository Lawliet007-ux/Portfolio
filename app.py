import streamlit as st
import base64

# 1. Set up a professional page configuration
st.set_page_config(
    page_title="Khushi Choudhary | Art & Design Portfolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS to style the page and make the PDF full-screen
st.markdown("""
    <style>
    /* Hide top Streamlit branding banner and padding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    div.stButton > button:first-child {
        background-color: #1E459F;
        color: white;
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Clean, professional header layout
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Khushi Choudhary")
    st.subheader("Artist & Designer | Applied Arts Portfolio")
with col2:
    st.write("") # Spacing
    # Simple download button for your visitors
    with open("pdf24_converted_compressed.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Full Portfolio PDF",
            data=file,
            file_name="Khushi_Choudhary_Portfolio.pdf",
            mime="application/pdf"
        )

st.write("---")

# 4. Embed the PDF completely seamlessly 
def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Use an iframe to let the browser display it natively with nothing else wrapping it
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="950px" style="border:none;"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Call the function with your exact file name
display_pdf("pdf24_converted_compressed.pdf")
