import requests
import os

"""
Send a GeekMail message

The referer header is required for the message to send correctly.
A few of the data fields may not be required, but they are included
when a "real" geekmail message is sent
"""


def send_geekmail(to, subject, body):
    # This is not actually a password, but rather the "bggpasword" cookie value
    BGG_PASSWORD = os.getenv("BGG_PASSWORD")
    BGG_USERNAME = os.getenv("BGG_USERNAME")
    BGG_SESSION_ID = os.getenv("BGG_SESSION_ID")

    resp = requests.post(
        "https://boardgamegeek.com/geekmail_controller.php",
        cookies={
            "bggpassword": BGG_PASSWORD,
            "bggusername": BGG_USERNAME,
            "SessionID": BGG_SESSION_ID,
        },
        data={
            "touser": to,
            "subject": subject,
            "body": body,
            "action": "save",
            "savecopy": 1,
            "sizesel": 10,
            "B1": "Send",
            "folder": "inbox",
            "ajax": 1,
            "searchid": 0,
            "pageid": 0,
        },
        headers={"Referer": "https://boardgamegeek.com/geekmail"},
    )
