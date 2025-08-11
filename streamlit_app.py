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

# Set a nice background image with CSS
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1350&q=80");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Pick or get the current quote
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

if st.button("Generate New Quote"):
    st.session_state.quote = random.choice(quotes)

# Show quote as big header
st.markdown(f"<h1 style='color: white; text-shadow: 2px 2px 4px #000000;'>{st.session_state.quote}</h1>", unsafe_
