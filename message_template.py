#############################################################################
#
#   chief delphi slack bot
#   message_template.py
#   written by siddharth lohani 
#   june 17th, 2021
#
#############################################################################

from datetime import datetime
import requests

def createPayload(latest_technical_post):

    data = {

        "attachments": [
            {
                "color": "#c55100",
                "blocks": [
                    {
                        "type": "header",
                                "text": {
                                    "type": "plain_text",
                                    "text": "[Technical] " + latest_technical_post["fancy_title"],
                                    "emoji": True
                                }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                                "fields": [
                                    {
                                        "type": "mrkdwn",
                                        "text": "*Created On:*\n " + datetime.fromisoformat(latest_technical_post["created_at"].replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M:%S %p')
                                    },
                                    {
                                        "type": "mrkdwn",
                                        "text": "*Likes:*\n " + str(latest_technical_post["like_count"])
                                    }
                                ]
                    },
                    {
                        "type": "section",
                                "fields": [
                                    {
                                        "type": "mrkdwn",
                                        "text": "*Updated On:*\n " + datetime.fromisoformat(latest_technical_post["last_posted_at"].replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M:%S %p')
                                    },
                                    {
                                        "type": "mrkdwn",
                                        "text": "*Replies:*\n " + str(latest_technical_post["posts_count"]-1)
                                    }
                                ]
                    },
                    {
                        "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                            "text": "*Description:* " + latest_technical_post["excerpt"].replace('&hellip;', '...') + '<https://chiefdelphi.com/t/' + latest_technical_post["slug"] + "/" + str(latest_technical_post["id"]) + '|View More>'
                                },
                        "block_id": "text1"
                    },
                ]
            }
        ]
    }

    return data

def test_data():
    assert createPayload(requests.get("https://www.chiefdelphi.com/c/technical/9/l/latest.json").json()['topic_list']['topics'][1])
