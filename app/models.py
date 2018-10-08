class Source:
    """News Source class to define Source Object"""
    def __init__(self, id, name,description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

    '''
        1. ID - The name of the news source according to its identification tag, e.g BBC-news, CNN, ABC
        2. name - The actual name of the news company
        3. description - A brief description of the new company
        4. url - The URL link or website to the news company 
        5. category - The category of news ,e.g entertainment, business, technology
        6. country - The country that the news originates from, e.g ABC News is from USA
        '''
class Article:
    '''
    class to define news article objects
    '''

    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
