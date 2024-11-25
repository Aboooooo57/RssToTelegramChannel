import feedparser


def fetch_rss(feed_url):
    feed = feedparser.parse(feed_url)
    return feed.entries
