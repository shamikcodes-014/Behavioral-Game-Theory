def imports():
    global pd,np, pk, loaded_model, load_min_max, loaded_nlp
    import pandas as pd
    import numpy as np
    import pickle as pk
    # import spacy
    # nlp=spacy.load("en_core_web_lg")
    loaded_nlp=pk.load(open('nlp.pkl', 'rb'))
    loaded_model=pk.load(open('gm_bhv_thy.pkl','rb'))
    load_min_max=pk.load(open('min_max_gm.pkl', 'rb'))
    

def predict(text):
    sr=pd.Series([text])
    vec=sr.apply(lambda x: loaded_nlp(x).vector)
    vec_2d=np.stack(vec)
    vec_scaled=load_min_max.transform(vec_2d)
    pred=loaded_model.predict(vec_scaled)
    return(pred)

