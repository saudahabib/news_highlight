from flask import render_template
from . import main
from ..request import get_sources, get_source, get_articles
from ..models import Article, Source
#Views
@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    sources = get_sources()
    articles = get_articles('kenya')
    title = "All the spice, under one roof"


    return render_template('index.html', title = title, sources = sources, articles = articles)

@main.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns page with news
    '''
    return render_template('news.html', id = news_id)


@main.route('/source/<int:id>')
def source(id):

    '''
    View source page function that returns the source details page and its data
    '''
    source = get_source(id)
    name = f'{source.name}'

    return render_template('news.html',name = name, source = source)
