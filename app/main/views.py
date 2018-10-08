from flask import render_template, request, redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    """View page for the function that returns the index"""
    general_news = get_sources('general')[0:5]

    message = "Welcome to the news room"
    title = "Welcome to the ultimate news room"

    return render_template('index.html',general = general_news,message = message, title = title)

@main.route('/articles/<id>')
def articles(id):
    '''
       View  page function that returns the details page and its data
       '''
    name = "melissamalala"
    articles = get_articles(id)

    return render_template('article.html', articles=articles, name=name, name_source=id)

