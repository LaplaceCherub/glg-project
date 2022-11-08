from flask import Flask, redirect, url_for, render_template, request
import spacy
import pickle
import pandas as pd
import gensim
import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/try/', methods=['POST', 'GET'])
def try_out():
    if request.method == 'POST':
        text = request.form.get('text')
    
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
            return return_list
        df_list = sentence_preprocessor(text)
        intermediate_df = pd.DataFrame(df_list, columns=['WordBase', 'WordLemma', 'WordPOS', 'WordTag', 
        'WordDep', 'WordLength', 'IsCapitalized', 'NonPunctuation', 'IsStop', 'PossibleNER'])
        pipeline = pickle.load(open('ner_model.pkl', 'rb'))
        preds = pipeline.predict(intermediate_df)
        rtn_ners = []
        for pred, word in zip(preds, df_list):
            if pred == 1:
                rtn_ners.append(word[0])
        ner_opener = "The entities from the input are:"


        dct = pickle.load(open('dct.pkl', 'rb')) 
        lda_model = pickle.load(open('lda.pkl', 'rb'))   

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

        lda_opener = 'The clusters from the input are:'
        lda_text = get_topics(text, lda_model, dct)
    
        return render_template('try.html', ner_opener=ner_opener, ner_text=rtn_ners, lda_opener=lda_opener, lda_text=lda_text)
    return render_template('try.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)