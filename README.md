# askfm.py [![Test](https://github.com/utgwkk/askfm.py/actions/workflows/ci.yml/badge.svg)](https://github.com/utgwkk/askfm.py/actions/workflows/ci.yml) [![PyPI version](https://badge.fury.io/py/askfm.py.svg)](https://badge.fury.io/py/askfm.py)
Ask.fm crawler

## Install

```
$ pip install askfm.py
```

## Example

This program shows recent 25 answers of [ezoeryou](https://ask.fm/ezoeryou).

```python
import askfm
crawler = askfm.Crawler('ezoeryou')

for pair in crawler.crawl():
  print(pair.question, '->', pair.answer)
```

## Document

### `askfm.Crawler(username)`

Initializes ask.fm crawler.

* `username`: the username you want to crawl answers.

### `askfm.Crawler.crawl(page)`

Fetches at most 25 answers and returns iterator of list of answers.

* `page`: the offset page. The default value is `0`, this means crawing at the top of answers.

### `askfm.Crawler.pager(page)`

A generator that yields `askfm.Crawler.crawl(page)` continuously.
Uses like this:

```python
# offset_page is given
for page in crawler.pager(offset_page):
  for pair in page:
    print(pair.question, pair.answer)
```

* `page`: the offset page. The default value is `0`, this means crawing at the top of answers.

### `askfm.Answers`

An iterator of continuous `askfm.Pair` objects.

### `askfm.Pair`

An object representing for pair of question and answer.
You can get them with `askfm.Pair.question` and `askfm.Pair.answer`.
