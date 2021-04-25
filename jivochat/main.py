import os
import re
import time
import requests
from pathlib import Path
from dotenv import load_dotenv
from telegram import Bot
from telegram.utils.request import Request
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from flask import Flask, request, Response, json, jsonify
from jivochat.utils import resources
from loguru import logger


dotenv_path = os.path.join(Path(__file__).parent.parent, 'config/.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")

req = Request(
    connect_timeout=30.0,
    read_timeout=5.0,
    con_pool_size=8,
)
bot = Bot(
    token=TOKEN,
    request=req,
)

logger.add(
    "logs/info.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="100 MB",
    compression="zip",
)


def main(data, source):
    if 'event_name' not in data:
        if data['message']['type'] == 'text':
            user = data['recipient']['id']
            text = data['message']['text']
            if source == 'telegram':
                bot.send_message(user, text)
            # viber.send_messages(user, [
            #     TextMessage(
            #         text=text)
            #     ]
            # )
    else:
        user_id = str(re.findall(f'\[(.*?)\]', data['visitor']['name'])[0])
        if data['event_name'] == 'chat_accepted':
            bot.send_message(user_id, resources.operator_connected)
        if data['event_name'] == 'chat_finished':
            if resources.user_ended_chat not in str(data['plain_messages']):
                reply_markup = ReplyKeyboardRemove()
                bot.send_message(
                            chat_id=user_id,
                            text=resources.operator_ended_chat,
                            reply_markup=reply_markup)
                time.sleep(1)
                inline_keyboard = [[InlineKeyboardButton(text='Меню',
                                            callback_data='start')]]
                inline_buttons = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
                bot.send_message(
                            chat_id=user_id,
                            text=resources.final_touch,
                            reply_markup=inline_buttons)
    returned_data = {'result': 'ok'}
    return returned_data
