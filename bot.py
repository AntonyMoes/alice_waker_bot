# -*- coding: utf-8 -*-

import botHandler
import os
import socket


greet_bot = botHandler.BotHandler("594760722:AAE_epRLd_DYiag967BWF6bu9zeBebspQxw")
s = socket.socket()
print(os.environ)
s.bind(('', int(os.environ.get("PORT", 4469))))
print("sock opening")
s.listen(1)
print("sock opened successfully")


def main():
    greet_bot.work()

<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == '__main__':  
>>>>>>> 2d1d3713fcb18672e4554ff5b3b208527405c0f6
    try:
        main()
    except KeyboardInterrupt:
        exit()