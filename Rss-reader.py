import feedparser


def parseRSS(rss_url):
    return feedparser.parse(rss_url)


def getHeadlines(rss_url):
    headlines = []

    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
        headlines.append(newsitem['link'])
        #headlines.append(newsitem['id'])
        #headlines.append(newsitem['summary'])
        #headlines.append(newsitem['published'])

    return headlines


allheadlines = []

newsurls = {

    'googlenews': 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru',


}

for key, url in newsurls.items():
    allheadlines.extend(getHeadlines(url))

for hl in allheadlines:
    print(hl)