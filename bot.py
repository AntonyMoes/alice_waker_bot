# -*- coding: utf-8 -*-

import botHandler
import datetime
import os
import socket


greet_bot = botHandler.BotHandler("594760722:AAE_epRLd_DYiag967BWF6bu9zeBebspQxw")
greetings = ('hello', 'hi', 'heya', 'howdy', 'привет', 'хей', 'здравствуйте', 'приветствую', 'хай')
now = datetime.datetime.now()
s = socket.socket()
print(os.environ)
s.bind(('', int(os.environ.get("PORT", 4469))))
print("sock opening")
s.listen(1)
print("sock opened successfully")


def main():
    new_offset = None


    while True:
        print("about to get updates")
        greet_bot.get_updates(new_offset)
        print("updates recieved")

        last_update = greet_bot.get_last_update()
        if last_update == [] :
            continue

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        hour = (now.hour + 3) % 24

        if last_chat_text.lower() in greetings:
            if 4 <= hour < 12:
                greeting = "Доброе утро"

            elif 12 <= hour < 17:
                greeting = "Добрый день"

            elif 17 <= hour < 23:
                greeting = "Добрый вечер"

            else:
                greeting = "Доброй ночи"

            greet_bot.send_message(last_chat_id,
                               "%s, %s\nТекущее время: %d:%d:%d" %
                               (greeting, last_chat_name, hour, now.minute, now.second))

        new_offset = last_update_id + 1


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
