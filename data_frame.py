from wiki_text import text_wiki_api
import spacy_streamlit
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

spacy_model = "en_core_web_sm"
# text=text_wiki_api()
def dataframe(text,spacy_model):
    
    doc = spacy_streamlit.process_text(spacy_model, text)
    d={}
    words=[]
    freqs=[]
    for ent in doc.ents:
        #print(ent.label_)
        if ent.label_ in d.keys():
            d[ent.label_] +=1
        else:
            d[ent.label_] = 1
    e={"words":d.keys(),"freqs":d.values()}
    df=pd.DataFrame.from_dict(e)

    return df
