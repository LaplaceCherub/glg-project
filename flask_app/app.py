from flask import Flask, redirect, url_for, render_template, request
import pickle
import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string

from utils import sentence_preprocessor

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

        ##### NER Model #####

        df_list, intermediate_df = sentence_preprocessor(text)

        with open('ner_model.pkl', 'rb') as ner_f:
            pipeline = pickle.load(ner_f)
        preds = pipeline.predict(intermediate_df)

        rtn_ners = []
        for pred, word in zip(preds, df_list):
            if pred == 1:
                rtn_ners.append(word[0])
        
            ## add spacy ner model here. 

        ##### LDA Model #####
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

        lda_text = get_topics(text, lda_model, dct)
    
        return render_template('try.html', requested=True, ner_text=rtn_ners, lda_text=lda_text)
    return render_template('try.html', requested=False)

if __name__ == '__main__':
    app.run(debug=True, port=8000)