# coding: utf-8
import unittest
import time
import requests
import askfm.parser
import six

class ParserTest(unittest.TestCase):
    def test_parse_question(self):
        html = requests.get('http://ask.fm/ezoeryou/answers/more?page=2').text
        result = askfm.parser.parse(html)
        self.assertEqual(len(result), 25)
        self.assertEqual(result[0].id, 135859194711)
        self.assertEqual(result[0].question, u'おいC++エヴァンゲリオン、C++ではなくSwiftを選ぶGoogleを許していいのか？')
        self.assertEqual(result[0].answer, u'Swiftは罠がありそうで怖い。')

if __name__ == '__main__':
    unittest.main()
