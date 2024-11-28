import re
import html
from bs4 import BeautifulSoup
from rss import fetch_rss
from telegram import send_image_to_telegram, send_message_to_telegram
from db import check_news_exists, insert_news_db, connect_db, create_table
from dotenv import load_dotenv
from utils import datetime_to_jalali, get_uid_news
import html

load_dotenv()

from settings import RSS_URL


async def drive():
    feed = fetch_rss(RSS_URL)

    with connect_db('news.db') as conn:
        create_table(conn)

        for entry in feed[::-1]:
            uid = get_uid_news(entry.id)
            if check_news_exists(conn, uid):
                continue

            title = entry.title
            link = entry.link
            description = clean_description(entry.description)
            pub_date = datetime_to_jalali(entry.published_parsed)
            image_url = entry.enclosures[0].get("url", "") if entry.enclosures else ""
            formatted_link = f"[ادامه مطلب]({link})"

            message = f"📢 {title}\n تاریخ انتشار:{pub_date[::-1].__repr__()}\n\n{description} ...\n\n{formatted_link}"

            try:
                if image_url:
                    await send_image_to_telegram(image_url, message)
                else:
                    await send_message_to_telegram(message)

                insert_news_db(conn, uid, title, description)

            except Exception as e:
                print(f"Problem while Send Or inserting news {e} ")


def clean_description(description):
    description = description.replace('&zwnj;', " ")
    soup = BeautifulSoup(description, "html.parser")
    clean_text = html.unescape(soup.get_text(strip=True))
    clean_text = ' '.join(clean_text.split())

    return clean_text
