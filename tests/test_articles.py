import unittest
from app.models import Article
# Article = articles.Article

class ArticleTest(unittest.TestCase):
    '''
        Test Class to test the behaviour of the Article class
        '''
    def setUp(self):
        '''
                Set up method that will run before every Test
                '''
        self.new_article = Article("the-wall-street-journal",
                                   "The Wall Street Journal",
                                   "Juan Montes",
                                   "U.S.-Mexico Trade Pact Faces Scrutiny From Lawmakers at Home",
                                   "The respective legislators, who ultimately must ratify the agreement.",
                                   "https:\/\/www.wsj.com\/articles\/u-s-mexico-trade-pact-faces-scrutiny-from-lawmakers-at-home-1535621400",
                                   "https:\/\/images.wsj.net\/im-23753\/social",
                                   )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_article.id, "the-wall-street-journal")
        # self.assertEqual(self.new_article.name, "The Wall Street Journal")
        # self.assertEqual(self.new_article.author, "Juan Montes")
        self.assertEqual(self.new_article.title, "U.S.-Mexico Trade Pact Faces Scrutiny From Lawmakers at Home")
        self.assertEqual(self.new_article.description, "The respective legislators, who ultimately must ratify the agreement.")
        self.assertEqual(self.new_article.url, "https:\/\/www.wsj.com\/articles\/u-s-mexico-trade-pact-faces-scrutiny-from-lawmakers-at-home-1535621400")
        self.assertEqual(self.new_article.urlToImage, "https:\/\/images.wsj.net\/im-23753\/social")
        self.assertEqual(self.new_article.publishedAt, "2018-08-30T10:51:22Z")
#
# if __name__ == '__main__':
#      unittest.main()