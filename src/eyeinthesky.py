import sys
import time
import telepot
import io
from telepot.loop import MessageLoop
import matplotlib.pyplot as plt

"""
usage: $ python eyeinthesky.py <token> <ownerId>

This bot will reply only to a single owner.

"""


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if chat_id != ownerId:
        bot.sendMessage(chat_id, "Sorry, you can not control me.")
        bot.sendMessage(ownerId, "Somebody contacted me; Id = " + str(chat_id))
        return
    if command == "/start":
        bot.sendMessage(chat_id, "Hi, master")
    if command == "/temp":
        buffer = io.BytesIO()
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        bot.sendPhoto(chat_id, buffer, "Current temperature = ...\n" +
                                       "humidity = ...             ")
    elif command == "/pic":
        bot.sendMessage(chat_id, "Sending picture")
    else:
        bot.sendMessage(chat_id, "Huh???")


try:
    token = sys.argv[1]
    ownerId = int(sys.argv[2])
except IndexError:
    print("Initialization error")
    sys.exit(0)

bot = telepot.Bot(token)
bot.getMe()

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
