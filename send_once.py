import os, json, random, requests

BOT_TOKEN = os.getenv("8045818615:AAFLMIW_-mmN0aeKLPRpS9dqGH0tFgQpP_E")
CHAT_ID = os.getenv("-1003355965909")

with open("promos.json","r",encoding="utf-8") as f:
    promos = json.load(f)

promo = random.choice(promos)
text = f"*{promo.get('title')}*\n\n{promo.get('text')}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
resp = requests.post(url, data={"chat_id": CHAT_ID, "text": text, "parse_mode":"Markdown"})
print(resp.status_code, resp.text)
