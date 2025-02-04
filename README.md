# NER-on-Wikipedia pages
## Wikipedia Api
Wikipedia-API is easy to use Python wrapper for Wikipedias’ API. It supports extracting texts, sections, links, categories, translations, etc from Wikipedia. Documentation provides code snippets for the most common use cases.


# Process 
* Take input query from web and find out related page on Wikipedia as Text
* Perforn Name Entity recognition task on Text and render them with their annoted class
* Plot visualization curve for labels frequency. 

# Package and Tools
* Streamlit, Spacy, Pandas, Matplotlib, Seaborn, Wikipedia-API, Heroku app



```import wikipediaapi 

def text_wiki_api(input_text):
    wiki_text = wikipediaapi.Wikipedia('en')
    page_py = wiki_text.page(input_text)
    
    print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True
    wiki_wiki = wikipediaapi.Wikipedia(language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI)
    p_wiki = wiki_wiki.page(input_text)
    text_fin = p_wiki.text

    return text_fin
```
#### This will return text for input query and further that will be used for text annotating.



![NER](https://github.com/SqweeksOp/NER-on-Wikipedia-_API/blob/main/Screenshot%20(4).png)
![NER WITH WORD FREQ](https://github.com/SqweeksOp/NER-on-Wikipedia-_API/blob/main/Screenshot%20(3).png)


