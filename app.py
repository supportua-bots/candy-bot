import functools
import subprocess
from flask import Flask, request, Response, json, jsonify
from multiprocessing import Process
from threading import Thread
from telegrambot import main as tgbot
from jivochat import main as jivo
from vibertelebot import main as vbbot


app = Flask(__name__)


def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                subprocess.call(
                    ["expect", "/var/www/chatbots2021/candy-bot/restart"])
    return wrapper


@error_handler
@app.route('/jivochatgram', methods=['GET', 'POST'])
def jivochat_endpoint_telegram():
    source = 'telegram'
    data = request.get_json()
    print(data)
    Thread(target=jivo.main, args=(data, source)).start()
    returned_data = {'result': 'ok'}
    response = app.response_class(
        response=json.dumps(returned_data),
        status=200,
        mimetype='application/json'
    )
    return response


@error_handler
@app.route('/jivochatviber', methods=['GET', 'POST'])
def jivochat_endpoint_viber():
    source = 'viber'
    data = request.get_json()
    print(data)
    Thread(target=jivo.main, args=(data, source)).start()
    returned_data = {'result': 'ok'}
    response = app.response_class(
        response=json.dumps(returned_data),
        status=200,
        mimetype='application/json'
    )
    return response


@error_handler
@app.route('/viber', methods=['POST'])
def viber_endpoint():
    source = 'viber'
    vbbot.main(request)
    return Response(status=200)


@error_handler
def server_launch():
    app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    # flask_server = Process(target=server_launch).start()
    # telegram_bot = Process(target=tgbot.main).start()
    try:
        flask_server = Process(target=server_launch).start()
        telegram_bot = Process(target=tgbot.main).start()
    except KeyboardInterrupt:
        flask_server.terminate()
        telegram_bot.terminate()
        flask_server.join()
        telegram_bot.join()
