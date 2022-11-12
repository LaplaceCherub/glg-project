from flask import Flask, redirect, url_for, render_template, request

from models import get_ners, get_topics

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
        ner_text = get_ners(text)         
        lda_text = get_topics(text)
        return render_template('try.html', requested=True, ner_text=ner_text, lda_text=lda_text)
    return render_template('try.html', requested=False)

if __name__ == '__main__':
    app.run(debug=True, port=8000)