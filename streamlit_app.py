import streamlit as st
import random

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "You learn more from failure than from success.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it."
]

# Gradient background CSS for whole page and transparent Streamlit containers
page_bg_style = """
<style>
/* Make the whole page background a colorful gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
    min-height: 100vh;
}

/* Make the main content container transparent so background shows through */
[data-testid="stMainContainer"] {
    background-color: rgba(255, 255, 255, 0.0);
    padding-top: 50px;
}

/* Center and style the button */
.stButton > button {
    background-color: #ff7e5f;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}

.stButton > button:hover {
    background-color: #feb47b;
}

/* Style the quote text */
h1 {
    color: white !important;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.6);
    text-align: center;
}
</style>
"""

st.markdown(page_bg_style, unsafe_allow_html=True)

# Initialize or get current quote from session state
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

if st.button("Generate New Quote"):
    st.session_state.quote = random.choice(quotes)

# Show quote as big header
st.markdown(f"<h1>{st.session_state.quote}</h1>", unsafe_allow_html=True)
