import pandas as pd
import spacy
import pickle
import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

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

def get_ners_reg(text):
    '''
    return the list of Named Entities in text from our model
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

def get_ners(text):
    '''
    return a list of Named Entities from the text combined from our model and spacy.ents . 
    '''
    tokens = nlp(text)
    spacy_ners = [ent.text for ent in tokens.ents]
    our_ners = get_ners_reg(text)
    # spacy picks up entities with more than one words
    spacy_ners_words_list = [word for ner_phrase in spacy_ners for word in ner_phrase.split()]
    for ner in our_ners:
        if ner.text not in spacy_ners_words_list:
            spacy_ners.append(ner.text)
    return spacy_ners

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

topics_dict = {
    0: ['vote', 'bird', 'election', 'flu'], 
    1: ['north', 'south', 'korea', 'prime', 'minister'],
    2: ['Beijing', 'Britain', 'France', 'gas', 'German', 'Middle', 'East', 'Russian'], 
    3: ['attack', 'military', 'bomb', 'force'],
    4: ['Iran', 'United', 'State', 'nuclear', 'European'],
    5: [ 'police', 'force', 'city', 'Muslim', 'security' ], 
    6: ['party', 'president', 'election', 'leader'], 
    7: ['woman', 'citizen', 'explosive'],
    8: ['Israeli', 'Islamic', 'militant'],
    9: ['economic', 'economy', 'price', 'world'],
    10: ['Lebanon', 'responsibility', 'explosion', 'group'],
    11: ['government', 'Israel', 'Palestinian','peace'], 
    12: ['United', 'State', 'secretary', 'storm', 'hurricane', 'emergency'],
    13: ['charge', 'right', 'court', 'Iraq', 'house'],
    14: ['oil', 'company',  'market', 'demand', 'power', 'government'],
}

def get_topics(text): 
    '''
    text: str
    return: a list of (topic_num, topic_percentage)
    '''
    with open('dct.pkl', 'rb') as dct_f:
        dictionary = pickle.load(dct_f)
    with open('lda.pkl', 'rb') as lda_f:
        lda_model = pickle.load(lda_f)
    
    text_doc = lda_sent_process(text)
    topics = lda_model[dictionary.doc2bow(text_doc)]
    topics.sort(key=lambda x: x[-1], reverse=True)
    for idx, (topic_num, percentage) in enumerate(topics):
        percentage = "{:2.2%}".format(percentage)
        topics[idx] = (topic_num, percentage)
    return topics if len(topics) <=4 else topics[:4]

####### KNN + Transformer Model ###########

def get_near_sent(text):
    with open('emb_model.pkl', 'rb') as emb_f:
        emb_model = pickle.load(emb_f)
    with open('knn_model.pkl', 'rb') as knn_f:
        knn_model = pickle.load(knn_f)   
    sentences_df = pd.read_csv('static/sentences.csv')

    embedding = emb_model.encode([text])
    _, index = knn_model.kneighbors(embedding)
    near_sent = []
    for idx in range(index.shape[1]):
        near_sent.append(sentences_df['Sentences'][index[0,idx]])
    return near_sent

if __name__ == '__main__':
    text = 'Mail Ballots Around Las Vegas Are Likely to Put Democrats Ahead.'
    topics = get_near_sent(text)

    print(topics)