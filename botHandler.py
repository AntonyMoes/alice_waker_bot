# -*- coding: utf-8 -*-

import requests
import datetime

<<<<<<< HEAD
greetings = ('hello', 'hi', 'heya', 'howdy', 'привет', 'хей',
             'здравствуйте', 'приветствую', 'хай', 'приветик', 'hey', 'здравствуй')

=======
greetings = ('hello', 'hi', 'heya', 'howdy', 'привет', 'хей', 'здравствуйте', 'приветствую', 'хай')
>>>>>>> 2d1d3713fcb18672e4554ff5b3b208527405c0f6
tips = ('Не ложитесь так поздно, как разработчик этого бота :^)',)


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.subscribers = {}

    def get_updates(self, offset=None, timeout=20):
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

    def work(self):
        new_offset = None

        while True:
            now = datetime.datetime.now()
            actual_hour = (now.hour + 3) % 24
            for k in self.subscribers.keys():
                if self.subscribers[k] == (actual_hour, now.minute):
                    self.send_message(k, "Просыпайся! Вперед к великим делам :3")
                    self.del_alarm(k)

            print("about to get updates")
            self.get_updates(new_offset)
            print("updates recieved")

            last_update = self.get_last_update()
            if last_update == []:
                continue

            update_id = last_update['update_id']
            text = last_update['message']['text']
            id = last_update['message']['chat']['id']
            name = last_update['message']['chat']['first_name']

            self.handle_request(text, id, name)

            new_offset = update_id + 1

    def handle_request(self, request, id, name):
        if request == "/start":
            self.add_subscriber(id)
        elif request == "/menu":
            self.send_message(id, self.menu())
<<<<<<< HEAD
        elif request == "/greet" or request in greetings:
=======
        elif request == "/greet":
>>>>>>> 2d1d3713fcb18672e4554ff5b3b208527405c0f6
            self.greet(id, name)

        elif request == "/alarmdel":
            self.del_alarm(id)

        elif request == "/tip":
            self.show_tip(id)

        elif str(request).split(" ")[0] == "/alarmset" and len(str(request).split(" ")) == 2:
            self.set_alarm(id, str(request).split(" ")[1])

        else:
            self.send_message(id, "Запрос непонятен 6_9. /menu - вызов справки")

    def add_subscriber(self, subscriber_id):
<<<<<<< HEAD
        self.subscribers[subscriber_id] = None
=======
        self.subscribers[subscriber_id] = "null"
>>>>>>> 2d1d3713fcb18672e4554ff5b3b208527405c0f6

    def greet(self, id, name):
        now = datetime.datetime.now()

        hour = (now.hour + 3) % 24

        if 4 <= hour < 12:
             greeting = "Доброе утро"

        elif 12 <= hour < 17:
            greeting = "Добрый день"

        elif 17 <= hour < 23:
            greeting = "Добрый вечер"

        else:
            greeting = "Доброй ночи"

        self.send_message(id, "%s, %s\nТекущее время: %d:%d:%d" % (greeting, name, hour, now.minute, now.second))

    def set_alarm(self, id, raw_time):
        self.subscribers[id] = (int(raw_time.split(":")[0]), int(raw_time.split(":")[1]))

    def del_alarm(self, id):
        if id in self.subscribers.keys():
<<<<<<< HEAD
            self.subscribers[id] = None
=======
            self.subscribers[id] = "null"
>>>>>>> 2d1d3713fcb18672e4554ff5b3b208527405c0f6

    def show_tip(self, id):
        self.send_message(id, tips[0])

    def menu(self):
        return "/menu - вывод меню\n\
        /greet - приветствие от бота\n\
        /alarmset hh:mm - поставить будильник\n\
        /alarmdel - удалить будильник\n\
        /tip - случайная заметка"