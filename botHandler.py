# -*- coding: utf-8 -*-

import requests


class BotHandler:

    subscribers = {}

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        print(get_result)

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = []

        return last_update

    def handle_request(self, request):
        return True;

    def menu(self):
        return "/menu - вывод меню\n\
        /greet - приветствие от бота\n\
        /alarmset - поставить будильник\n\
        /alarmdel - удалить будильник\n\
        /tip - случайная заметка"