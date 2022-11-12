from flask import Flask, redirect, url_for, render_template, request
import pickle

from utils import sentence_preprocessor, get_topics

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
            ner_model = pickle.load(ner_f)
        preds = ner_model.predict(intermediate_df)
        rtn_ners = []
        for pred, word in zip(preds, df_list):
            if pred == 1:
                rtn_ners.append(word[0])
            ## add spacy ner model here. 

        ##### LDA Model #####
        with open('dct.pkl', 'rb') as dct_f:
            dictionary = pickle.load(dct_f)
        with open('lda.pkl', 'rb') as lda_f:
            lda_model = pickle.load(lda_f)
        lda_model = pickle.load(open('lda.pkl', 'rb'))   
        lda_text = get_topics(text, lda_model, dictionary)
    
        return render_template('try.html', requested=True, ner_text=rtn_ners, lda_text=lda_text)
    return render_template('try.html', requested=False)

if __name__ == '__main__':
    app.run(debug=True, port=8000)