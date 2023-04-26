from flask import Flask, request, url_for, flash, redirect
from flask import render_template


app = Flask(__name__)
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if title and content:
            messages.append({'title': title, 'content': content})
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/sources')
def sources():
	return render_template("sources.html")


if __name__ == '__main__':
    app.run()
