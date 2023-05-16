def func1():
    global nlp, pd, loaded_model
    import pandas as pd
    import spacy
    import pickle as pk
    nlp=spacy.load("en_core_web_lg")
    loaded_model=pk.load(open('gm_bhv_thy.pkl','rb'))

def func2():
    text="save people"
    sr=pd.Series([text])
    vec=sr.apply(lambda x: nlp(x).vector)
    print(vec)

