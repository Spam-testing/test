import streamlit as st
quotes=["hi","test","random"]
quote_of_the_day=random.choice(quotes)
print(quote_of_the_day)
quotes.remove(quote_of_the_day)
