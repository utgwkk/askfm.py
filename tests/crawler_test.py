import unittest
import time
import sys
sys.path.append('.')
import askfm
import six

class CrawlerTest(unittest.TestCase):
    def setUp(self):
        self.crawler = askfm.Crawler('ezoeryou')

    def tearDown(self):
        time.sleep(1)

    def test_generate_url(self):
        url = self.crawler.generate_url()
        self.assertEqual(url, 'http://ask.fm/ezoeryou/answers/more?page=0')

    def test_generate_url_with_page(self):
        url = self.crawler.generate_url(5)
        self.assertEqual(url, 'http://ask.fm/ezoeryou/answers/more?page=5')

    def test_crawl_without_page(self):
        datas = self.crawler.crawl()
        self.assertIsInstance(datas, askfm.Answers)
        for pair in datas:
            self.assertIsInstance(pair, askfm.Pair)
            self.assertIsInstance(pair.question, six.text_type)
            self.assertIsInstance(pair.answer, six.text_type)
            break

    def test_crawl_with_page(self):
        datas = self.crawler.crawl(1)
        self.assertIsInstance(datas, askfm.Answers)
        for pair in datas:
            self.assertIsInstance(pair, askfm.Pair)
            self.assertIsInstance(pair.question, six.text_type)
            self.assertIsInstance(pair.answer, six.text_type)
            break

    def test_crawl_with_large_page_returns_empty_answers(self):
        datas = self.crawler.crawl(100000000000000)
        self.assertIsInstance(datas, askfm.Answers)
        self.assertEqual(len(datas), 0)

    def test_pager(self):
        pager = self.crawler.pager()
        datas = next(pager)
        self.assertIsInstance(datas, askfm.Answers)
        datas = next(pager)
        self.assertIsInstance(datas, askfm.Answers)

    def test_pager_stops_when_reached_max_page(self):
        datas = self.crawler.pager(100000000000000)
        self.assertRaises(StopIteration, next, datas)

if __name__ == '__main__':
    unittest.main()
