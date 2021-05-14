import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import date, datetime, timedelta


dotenv_path = os.path.join(Path(__file__).parent.parent, 'config/.env')
load_dotenv(dotenv_path)

MAIN_COLOR = os.getenv("COLOR")


SHARE_PHONE_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": MAIN_COLOR,
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MAIN_COLOR,
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "operator",
            "ReplyType": "message",
            "Text": "Зв'язок з оператором",
            "TextOpacity": 0,
            "Image": 'https://i.ibb.co/6ZZqWPM/image.png'
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MAIN_COLOR,
            "BgLoop": True,
            "ActionType": "share-phone",
            "ActionBody": "phone_reply",
            "ReplyType": "message",
            "Text": "Подiлитись номером",
            "TextOpacity": 0,
            "Image": 'https://i.ibb.co/KzHgfzN/image.png'
        },
    ]
}
