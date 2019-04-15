from app import app
import urllib.request,json
from .models import source, article


# Getting the API key, base url and article base url
api_key = None
base_url = None
article_base_url = None

def configure_request(app):
    global api_key,base_url, article_base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    # print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results


def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            language = source_details_response.get('language')
            country = source_details_response.get('country')

            source_object = Source(name, description, url, language, country)


    return movie_object

def process_results(sources_list):
    '''
    Transforms the source results into a list of objects

    Args:
        sources_list = a list of dictionaries that contain article details

    Returns:
        sources_results
    '''

    sources_results = []
    for source in sources_list:
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        language = source.get('language')
        country = source.get('country')

        if url:
            source_object = Source(name, description, url, language, country)
            sources_results.append(source_object)

    return sources_results

def get_articles(query):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_base_url.format(query,api_key)
    # print(get_sources_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)


    return articles_results




def process_article_results(article_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain articles' details

    Returns :
        articles_results: A list of movie objects
    '''
    articles_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = Article(author, title, description, url, urlToImage,publishedAt)
            articles_results.append(article_object)

    return articles_results
