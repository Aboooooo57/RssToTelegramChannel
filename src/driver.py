import asyncio
import re
from rss import fetch_rss
from telegram import send_image_to_telegram, send_message_to_telegram
from db import check_news_exists, insert_news_db, connect_db, create_table
from dotenv import load_dotenv
from utils import datetime_to_jalali, get_uid_news
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
            description = re.sub(r'&amp;#13;|&amp;|&zwnj;|zwnj;|nbsp;|&nbsp;|laquo;|raquo;|zwnj|amp;|nbsp|', '',
                                 entry.description)
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


if __name__ == "__main__":
    asyncio.run(drive())
