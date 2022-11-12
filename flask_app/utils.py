import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string

####### NER Model Prepreocessor ###########

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

####### LDA Model Preprocesser ###########

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

def get_topics(new_text, lda_model, dct): 
    '''
    new_text: str
    lda_model: load from lda.pkl
    dct: load from dct.pkl
    '''
    rtn_list = []
    new_text_doc = lda_sent_process(new_text)
    topics = lda_model[dct.doc2bow(new_text_doc)]
    for topic in topics: 
        rtn_list.append(f'Topic {topic[0]} with probability {topic[1]}')
    return rtn_list