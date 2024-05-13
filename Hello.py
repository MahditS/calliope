from happytransformer import HappyTextToText
import streamlit as st
from pyaspeller import YandexSpeller
from happytransformer import TTSettings

speller = YandexSpeller()
happy_tt = HappyTextToText("T5",  "prithivida/grammar_error_correcter_v1")

"""
# Calliope
Grammar Correcting App
"""

inputText = st.text_input(label="Enter in message to be corrected")

text = "gec: " + inputText
settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
result = happy_tt.generate_text(text, args=settings)
result2 = happy_tt.generate_text(result.text, args=settings)

st.write(result2.text)