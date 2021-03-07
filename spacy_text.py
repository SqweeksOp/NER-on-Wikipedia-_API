from wiki_text import text_wiki_api
import spacy_streamlit
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
from visual import plot_freqdist_freq_bar
from data_frame import dataframe

spacy_model = "en_core_web_sm"


st.set_page_config(layout="wide")
st.title("Wikipedia  Name Entity Analysis")

st.markdown("""
This app performs  name entity recognition on wikipedia pages.

* **Data source:** [Wikipedia.com](https://www.wikipedia.com/).
""")
st.sidebar.header('Tasks')
list_comment_type = ["Name Entity Recognition","NER with Frequency Graph"]
comment_type = st.sidebar.selectbox('Type of Comments', list_comment_type)
input_text = st.text_area("Enter Text Here(Press ctrl+enter)","India")
Text = text_wiki_api(input_text)


# @st.cache
def load_data(Text, comment_type=comment_type):
    doc = spacy_streamlit.process_text(spacy_model, Text)
    spacy_streamlit.visualize_ner(doc,
    show_table=False,
    labels=["PERSON","DATE","GPE","FAC","LANGUAGE","LAW","NORP","ORDINAL","ORG","PERCENT","PRODUCT"],
    title="Persons, dates, locations, Product and Organisation")
    if comment_type == "Name Entity Recognition":
        # doc = spacy_streamlit.process_text(spacy_model, Text)
        # spacy_streamlit.visualize_ner(doc,
        # show_table=False,
        # labels=["PERSON","DATE","GPE","FAC","LANGUAGE","LAW","NORP","ORDINAL","ORG","PERCENT","PRODUCT"],
        # title="Persons, dates, locations, Product and Organisation")
        
        return st.text(f"Analyzed using spaCy model {spacy_model}")

        
    
    if comment_type == "NER with Frequency Graph":
        df = dataframe(Text,spacy_model)
        return plot_freqdist_freq_bar(df,title='Frequency plot')

Text = text_wiki_api(input_text) 
load_data(Text,comment_type)
# Text = st.text_area("Text to analyze", text, height=200)
# doc = spacy_streamlit.process_text(spacy_model, Text)

