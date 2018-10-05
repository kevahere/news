from flask import render_template, request, redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    """View page for the function that returns the index"""
    general_news = get_sources('general')[0:5]

    message = "Welcome to the news room"
    title = "Welcome to the ultimate news room"

    return render_template('index.html',general = general_news,)