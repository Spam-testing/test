import streamlit as st
import random

# List of quotes
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

st.title("Random Quote Generator")

# Initialize or get current quote from session state
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

# Small button to generate a new quote
if st.button("Generate New Quote"):
    st.session_state.quote = random.choice(quotes)

st.write(f"> {st.session_state.quote}")
