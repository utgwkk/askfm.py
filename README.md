# askfm.py [![Build Status](https://travis-ci.org/utgwkk/askfm.py.svg?branch=master)](https://travis-ci.org/utgwkk/askfm.py)
Ask.fm crawler

## Install

```
$ pip install askfm.py
```

## Example

This program shows recent 25 answers of [ezoeryou](http://ask.fm/ezoeryou).

```python
import askfm
crawler = askfm.Crawler('ezoeryou')

for pair in crawler.crawl():
  print(pair.question, '->', pair.answer)
```
