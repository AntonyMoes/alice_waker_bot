import botHandler
import datetime
import os
import socket


greet_bot = botHandler.BotHandler("594760722:AAE_epRLd_DYiag967BWF6bu9zeBebspQxw")
greetings = ('hello', 'hi', 'heya', 'howdy')
now = datetime.datetime.now()
s = socket.socket()
print(os.environ)
s.bind(('', int(os.environ.get("PORT", 4469))))
print("sock opening")
s.listen(1)
print("sock opened successfully")


def main():
    new_offset = None
    today = now.day
    hour = now.hour
    minute = now.minute

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

        if last_chat_text.lower() in greetings  and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good morning, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings  and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good day, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings  and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good evening, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
