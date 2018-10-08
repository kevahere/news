import urllib.request, json
from .models import Source, Article

#Getting api key
api_key = None
base_url = None
articles_url = None

def configure_request(app):

    global api_key, base_url, articles_url
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

def get_articles(id):
    """Getting json response from url"""
    get_article_details_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        articles_results = None
        if article_details_response['articles']:
            article_results_list = article_details_response['articles']

            articles_results = process_articles(article_results_list)

    return articles_results

def process_articles(articles_list):
    article_results = []
    for article in articles_list:
        id = article['source']['id']
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        if url:
            articles_object = Article(id,
                                      author,
                                      title,
                                      description,
                                      url,
                                      urlToImage,
                                      publishedAt)
            article_results.append(articles_object)

    return article_results