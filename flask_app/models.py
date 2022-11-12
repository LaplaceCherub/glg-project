import pandas as pd
import spacy
import pickle

import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string

####### NER Model ###########

nlp = spacy.load('en_core_web_sm')

def sentence_preprocessor(text):
    return_list = []
    words = nlp(text)
    for word in words:
        word_base = word
        word_lemma = word.lemma_
        word_pos = word.pos_
        word_tag = word.tag_
        word_dep = word.dep_
        word_length = len(word)
        word_capitalization = str(word)[0].isupper()
        word_punctiation = str(word).isalnum()
        word_stop = word.is_stop
        is_ner = str(word) in set(ent.text for ent in words.ents)
        return_list.append((word_base, word_lemma, word_pos, word_tag, word_dep, 
        word_length, word_capitalization, word_punctiation, word_stop, is_ner))
    
    columns=['WordBase', 'WordLemma', 'WordPOS', 'WordTag', 'WordDep', 'WordLength', 
            'IsCapitalized', 'NonPunctuation', 'IsStop', 'PossibleNER']

    intermediate_df = pd.DataFrame(return_list, columns=columns)

    return return_list, intermediate_df

def get_ners(text):
    '''
    return a list of Named Entities from the text. 
    '''
    df_list, intermediate_df = sentence_preprocessor(text)
    with open('ner_model.pkl', 'rb') as ner_f:
        ner_model = pickle.load(ner_f)
    preds = ner_model.predict(intermediate_df)
    ner_list = []
    for pred, word in zip(preds, df_list):
        if pred == 1:
            ner_list.append(word[0])
    return ner_list


####### LDA Model ###########

def _lemmatize_words(sentence):
    wordnet_map = {'N':wordnet.NOUN, 'V':wordnet.VERB, 'J':wordnet.ADJ, 'R':wordnet.ADV}
    pos_tagged_text = nltk.pos_tag(sentence.split())
    return ' '.join([WordNetLemmatizer().lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

def lda_sent_process(text):
    text = text.lower()  
    PUNCT_TO_REMOVE = string.punctuation
    text = text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))
    STOPWORDS = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])
    text = _lemmatize_words(text)
    return text.split()

def get_topics(text): 
    '''
    text: str
    lda_model: load from lda.pkl
    dct: load from dct.pkl
    '''
    with open('dct.pkl', 'rb') as dct_f:
        dictionary = pickle.load(dct_f)
    with open('lda.pkl', 'rb') as lda_f:
        lda_model = pickle.load(lda_f)
    
    rtn_list = []
    new_text_doc = lda_sent_process(text)
    topics = lda_model[dictionary.doc2bow(new_text_doc)]
    for topic in topics: 
        rtn_list.append(f'Topic {topic[0]} with probability {topic[1]}')
    return rtn_list