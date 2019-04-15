class Article:
    '''
    Article class to define article Objects
    '''

    def __init__(self,author, title, description, url, urlToImage,publishedAt ):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
