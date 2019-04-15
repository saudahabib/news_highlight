import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Jake clinton', 'The lord of earth', 'description', 'http://lololo.com', 'http://lololoimage.com','2019-04-08T18:44:22Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
