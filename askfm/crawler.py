import requests
from .answers import Answers


class Crawler:
    def __init__(self, username):
        self._username = username

    def generate_url(self, page=0):
        return 'http://ask.fm/{}/answers/more?page={}' \
                .format(self._username, page)

    def crawl(self, page=0):
        res = requests.get(self.generate_url(page))
        if 300 <= res.status_code:
            return Answers('')
        retval = Answers(res.text)
        return retval

    def pager(self, page=0):
        while True:
            val = self.crawl(page)
            if len(val) <= 0:
                break
            yield val
            page += 1
