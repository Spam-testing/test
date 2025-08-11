import streamlit as st

import random


quotes=["hi","test","random"]
quote_of_the_day=random.choice(quotes)
print(quote_of_the_day)
quotes.remove(quote_of_the_day)

st.title(quote_of_the_day)
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
