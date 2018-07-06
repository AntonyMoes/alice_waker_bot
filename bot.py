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
        last_chat_text = last_chat_text.decode("ASCII")
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_name = last_chat_name.decode("ASCII")

        if last_chat_text.lower() in greetings  and 6 <= now.hour < 12:
            greet_bot.send_message(last_chat_id,
                                   "Доброе утро, %s\nТекущее время: %d:%d:%d" %
                                   (last_chat_name, now.hour, now.minute, now.second))

        elif last_chat_text.lower() in greetings  and 12 <= now.hour < 17:
            greet_bot.send_message(last_chat_id,
                                   "Добрый день, %s\nТекущее время: %d:%d:%d" %
                                   (last_chat_name, now.hour, now.minute, now.second))

        elif last_chat_text.lower() in greetings  and 17 <= now.hour < 23:
            greet_bot.send_message(last_chat_id,
                                   "Добрый вечер, %s\nТекущее время: %d:%d:%d" %
                                   (last_chat_name, now.hour, now.minute, now.second))

        new_offset = last_update_id + 1


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
