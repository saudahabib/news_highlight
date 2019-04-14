from flask import render_template
from app import app
from .request import get_sources
#Views
@app.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    sources = get_sources()
    
    title = "All the spice, under one roof"
    message = "Hello World"
    tags = "Tag, You're it!"

    return render_template('index.html', message = message, tags = tags, title = title, sources = sources)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns page with news
    '''
    return render_template('news.html', id = news_id)
