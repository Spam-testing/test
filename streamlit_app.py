import streamlit as st
import random
import string

def generate_code(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Initialize the code in session state if it doesn't exist
if "code" not in st.session_state:
    st.session_state.code = generate_code()

st.title("Random Code Generator")

if st.button("Generate New Code"):
    st.session_state.code = generate_code()

st.write(f"**Your random code:** {st.session_state.code}")
