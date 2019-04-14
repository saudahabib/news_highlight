import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('python world', 'flight set to crash again','It is ethiopian airlines', 'https://ichef.bbci.co.uk/news/1024/branded_news/B576/production/_106445464_ivanka2.png', 'Lorem ipsum dolor sit amet...')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()
