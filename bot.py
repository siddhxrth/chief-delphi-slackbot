#############################################################################
#
#   chief delphi slack bot
#   bot.py
#   written by siddharth lohani 
#   june 17th, 2021
#
#############################################################################

import requests, json, message_template, time, setup

headers = {
    'Content-type': 'application/json',
}

latest_techincal = requests.get("https://www.chiefdelphi.com/c/technical/9/l/latest.json").json()['topic_list']['topics']

previous_latest_topic = None

while True:
    latest_techincal = requests.get("https://www.chiefdelphi.com/c/technical/9/l/latest.json").json()['topic_list']['topics'][1]

    if (latest_techincal != previous_latest_topic):
        data = message_template.createPayload(latest_techincal)
        requests.post(setup.WEBHOOK_URL, headers=headers, data=json.dumps(data))
        previous_latest_topic = latest_techincal
        print("posted message")
    else:
        print ("no new messages")
    
    time.sleep(int(setup.REFRESH_INTERVAL))
