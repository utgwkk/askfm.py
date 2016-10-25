import os
from bs4 import BeautifulSoup
from .pair import Pair

def _href_to_id(href):
    return int(os.path.basename(href))

def parse(answers):
    '''parse given HTML from crawler.'''
    soup = BeautifulSoup(answers, 'html.parser')
    retval = []
    for div in soup.select('.streamItem-answer'):
        try:
            _id = _href_to_id(div.select('.streamItemContent-footer')[0].a.get('href'))
            question = div.select('.streamItemContent-question')[0].h2.string
            answer = div.select('.streamItemContent-answer')[0].string
            retval.append(Pair(_id, question, answer))
        except IndexError:
            pass
    return retval
