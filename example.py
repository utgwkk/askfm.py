import askfm
crawler = askfm.Crawler('ezoeryou')

for pair in crawler.crawl():
  print(pair.question, '->', pair.answer)
