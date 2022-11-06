from flask import Flask, redirect, url_for, render_template, request
import spacy
import pickle
import pandas as pd

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
        rtn_statement = "The entities from the input are:"
        return render_template('try.html', opener=rtn_statement, text=rtn_ners)
    return render_template('try.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)