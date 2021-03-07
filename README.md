# NER-on-Wikipedia-_API
## Wikipedia Api
Wikipedia-API is easy to use Python wrapper for Wikipedias’ API. It supports extracting texts, sections, links, categories, translations, etc from Wikipedia. Documentation provides code snippets for the most common use cases.


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

If you want to embed images, this is how you do it:

![NER](https://github.com/SqweeksOp/NER-on-Wikipedia-_API/blob/main/Screenshot%20(1).png)
![NER WITH WORD FREQ](https://github.com/SqweeksOp/NER-on-Wikipedia-_API/blob/main/Screenshot%20(2).png)


