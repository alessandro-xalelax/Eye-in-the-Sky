import sys
import time
import Image
import telepot
import io
from telepot.loop import MessageLoop
from cv2 import *
import matplotlib
matplotlib.use('agg')
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
        plt.gcf().clear()
        buffer = io.BytesIO()
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        bot.sendPhoto(chat_id, buffer, "Current temperature = ...\n" +
                                       "humidity = ...             ")
    elif command == "/pic":
        cam = VideoCapture(0)
        readSuccessful, img = cam.read()
	if readSuccessful:
            RGB_img = cvtColor(img, COLOR_BGR2RGB)
            buffer = io.BytesIO()
            image = Image.fromarray(RGB_img)
            image.save(buffer, format = "PNG")
            buffer.seek(0)
            bot.sendPhoto(chat_id, buffer)
        else:
            bot.sendMessage(chat_id, "Webcam error")
        cam.release()
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
