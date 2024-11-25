import httpx

from settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_USERNAME


async def send_image_to_telegram(image_url, caption):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    payload = {"chat_id": TELEGRAM_CHANNEL_USERNAME, "photo": image_url, "caption": caption, "parse_mode": "Markdown"}
    response, status_code = await post_data(url, payload)
    return response, status_code


async def send_message_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHANNEL_USERNAME, "text": text, "parse_mode": "Markdown"}
    response, status_code = await post_data(url, payload)
    return response, status_code


async def post_data(url, payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.text, response.status_code
