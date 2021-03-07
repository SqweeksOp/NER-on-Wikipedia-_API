#               Token Frequency Plot Bar
from wiki_text import text_wiki_api
import spacy_streamlit
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

#------------------------------------------------------------------------------------------------------------
def plot_freqdist_freq_bar(df, 
                       title='Frequency plot'):
    sns.set(style="ticks",
    rc={
        "figure.figsize": [17.5, 7.5],
        "text.color": "black",
        "axes.labelcolor": "black",
        "axes.edgecolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "axes.facecolor": "#c9ffd1",
        "figure.facecolor": "#c9ffd1"}
    )
    
    # df_1 = data_frame() 
    
    fig,ax = plt.subplots()
    ax = sns.barplot(x=df['freqs'], y=df['words'], palette="Blues_d", linewidth=0)
    plt.title("{}".format(title))
    degrees = 70
    plt.xticks(rotation=degrees)

    st.pyplot(fig)
    #plt.show()

    return 


