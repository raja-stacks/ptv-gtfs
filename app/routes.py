from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
        user = {'username': 'Raja'}

        posts = [
                {
                        'author': {'username': 'Raja'},
                        'body': 'Beautiful day in Melbourne!'
                },
                {
                        'author': {'username': 'Raja'},
                        'body': 'The Batman movie was so cool!'
                }
        ]

        return render_template('index.html', title='Home', user=user, posts=posts)