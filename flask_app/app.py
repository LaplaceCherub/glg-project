from flask import Flask, redirect, url_for, render_template, request

from models import get_ners, get_topics, get_near_sent, topics_dict

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
        topics = get_topics(text)
        nearest_text = get_near_sent(text)
        return render_template('try.html', requested=True, ner_text=ner_text, 
                topics = topics, nearest_text=nearest_text, topics_dict=topics_dict,
                original_sentence=text)
    return render_template('try.html', requested=False)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')