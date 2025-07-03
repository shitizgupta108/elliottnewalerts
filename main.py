import time
import schedule
import requests
import datetime

BOT_TOKEN = "7816564668:AAEOvjFwO7kqhK4EokIoQ40EHdygM_yU2e0"
CHANNEL_ID = "@elliottwavealerts"

def send_alert():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"🔔 15-min Elliott Wave Update ({now})\n\nNifty: Wave 3 possibly extending.\nCrude: Tracking minor Wave 4 pullback.\nNaturalGas: In Wave 5 thrust — tight SL advised."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL_ID, "text": message}
    requests.post(url, data=data)

schedule.every(15).minutes.do(send_alert)

# Initial alert
send_alert()

while True:
    schedule.run_pending()
    time.sleep(1)
