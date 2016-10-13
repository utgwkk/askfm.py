# coding: utf-8
import unittest
import six
from askfm import Pair


class PairTest(unittest.TestCase):
    def setUp(self):
        self.pair = Pair(u'ほほほほほ', u'質問ではない。')

    def test_dict_pair(self):
        self.assertDictEqual(dict(self.pair), {'question': u'ほほほほほ', 'answer': u'質問ではない。'})

if __name__ == '__main__':
    unittest.main()
