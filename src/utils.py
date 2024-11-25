from urllib.parse import urlparse, parse_qs

from convertdate import persian


def datetime_to_jalali(published_parsed):
    gregorian_date = (published_parsed.tm_year, published_parsed.tm_mon, published_parsed.tm_mday)
    jalali_date = persian.from_gregorian(*gregorian_date)
    return jalali_date


def get_uid_news(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('uid', [None])[0]
