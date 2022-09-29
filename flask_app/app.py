from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/try/')
def try_out():
    return render_template('try.html')

if __name__ == '__main__':
    app.run(debug=True)