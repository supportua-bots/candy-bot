import os
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import (ViberFailedRequest,
                                         ViberConversationStartedRequest,
                                         ViberMessageRequest,
                                         ViberSubscribedRequest)
from loguru import logger
from vibertelebot.handlers import user_message_handler
from vibertelebot.utils.tools import keyboard_consctructor
from telegrambot.utils import resources

dotenv_path = os.path.join(Path(__file__).parent.parent, 'config/.env')
load_dotenv(dotenv_path)


viber = Api(BotConfiguration(
    name='Test Bot',
    avatar='https://i.ibb.co/SPXsFsp/image.jpg',
    auth_token='4d32d064af27dc4e-1e05a35088b28256-ec7e6129925eb789'
))

logger.add(
    "logs/info.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="100 MB",
    compression="zip",
)


@logger.catch
def main(request):
    viber_request = viber.parse_request(request.get_data())
    # Defining type of the request and replying to it
    if isinstance(viber_request, ViberMessageRequest):
        user_message_handler(viber, viber_request)
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.user.id, [
            TextMessage(text="Дякую!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {viber_request}")
    elif isinstance(viber_request, ViberConversationStartedRequest):
        # First touch, sending to user keyboard with phone sharing button
        keyboard = [('Запис на відео чат', 'video', ''),
                    ("Зв'язок з оператором", 'operator', 'https://i.ibb.co/6ZZqWPM/image.png')]
        reply_keyboard = keyboard_consctructor(keyboard)
        viber.send_messages(viber_request.user.id, [
            TextMessage(
                text=resources.greeting_message,
                keyboard=reply_keyboard)
            ]
        )
