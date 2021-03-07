import wikipediaapi 

def text_wiki_api(input_text):
    wiki_text = wikipediaapi.Wikipedia('en')
    page_py = wiki_text.page(input_text)
    
    print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

    # page_missing = wiki_text.page('Python_(programming_language)')
    # print("Page - Exists: %s" %     page_missing.exists())



    wiki_wiki = wikipediaapi.Wikipedia(language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI)
    p_wiki = wiki_wiki.page(input_text)
    text_fin = p_wiki.text

    return text_fin

