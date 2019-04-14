from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting the API key
api_key = app.config['NEWS_API_KEY']

#Getting the news base URL
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    # print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            sources_results = process_results(sources_results_list)


    return sources_results



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
        author = source.get('author')
        title = source.get('title')
        urlToImage = source.get('urlToImage')
        description = source.get('description')
        content = source.get('content')

        if urlToImage:
            source_object = Source(author, title, urlToImage, description, content)
            sources_results.append(source_object)

    return sources_results
