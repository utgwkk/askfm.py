from bs4 import BeautifulSoup
from .pair import Pair

def parse(answers):
    '''parse given HTML from crawler.'''
    soup = BeautifulSoup(answers)
    retval = []
    for div in soup.select('.streamItem-answer'):
        question = div.select('.streamItemContent-question')[0].h2.string
        answer = div.select('.streamItemContent-answer')[0].string
        retval.append(Pair(question, answer))
    return retval
