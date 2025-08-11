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

# Gradient background CSS
gradient_bg = '''
<style>
body {
  background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
  height: 100vh;
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>
'''

st.markdown(gradient_bg, unsafe_allow_html=True)

# Initialize or get current quote from session state
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

if st.button("Generate New Quote"):
    st.session_state.quote = random.choice(quotes)

# Show quote as a big header with white color and shadow for readability
st.markdown(
    f"<h1 style='color: white; text-shadow: 2px 2px 6px rgba(0,0,0,0.7); text-align:center; margin-top: 100px;'>{st.session_state.quote}</h1>", 
    unsafe_allow_html=True
)
