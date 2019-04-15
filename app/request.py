from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting the API key
api_key = app.config['NEWS_API_KEY']

#Getting the news base URL and the article base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLES_API_BASE_URL"]

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
