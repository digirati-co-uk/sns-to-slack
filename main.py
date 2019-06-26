import requests
import json
import os


def alert_slack(webhook_url, message):
    _ = requests.post(webhook_url, json={
            "text": message["headline"],
            "link_names": 1,
            "attachments": [
                {
                    "text": message["detail"],
                    "color": message["color"],
                    "title": message["title"]
                }
            ]
        })


def lambda_handler(event, context):

    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    message = {
        "headline": event["Records"][0]["Sns"]["MessageAttributes"]["headline"]["Value"],
        "detail": event["Records"][0]["Sns"]["Message"],
        "color": event["Records"][0]["Sns"]["MessageAttributes"]["color"]["Value"],
        "title": event["Records"][0]["Sns"]["MessageAttributes"]["title"]["Value"]
    }

    print("about to post message " + json.dumps(message))

    alert_slack(webhook_url, message)

    return 0
