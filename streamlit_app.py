import streamlit as st

import random


quotes=["hi","test","random"]
quote_of_the_day=random.choice(quotes)
print(quote_of_the_day)
quotes.remove(quote_of_the_day)
