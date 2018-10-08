import urllib.request, json
from .models import Source

#Getting api key
api_key = None
base_url = None
articles_url = None

def configure_request(app):

    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_API_ARTICLE_BASE_URL']

def get_sources(category):
    """Function that gets the json response to our url request"""
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    """Process the news source results and transforms it to a list of objects"""
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,country)
            source_results.append(source_object)

    return source_results
