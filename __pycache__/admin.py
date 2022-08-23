import telebot
from  datetime import datetime
from telebot import types
from con.configuration import *
from con.classes.api.ApiRequests import ClassApis

bot = telebot.TeleBot(TOKEN)

class Administrator():
    def __init__(self):
        pass

    def log_id(self, bot):
        @bot.message_handler(content_types=["text"])
        def text(message):
            user_id = message.text
            bot.send_message(message.chat.id, "send my a photo ...")
            print(user_id)

            @bot.message_handler(content_types=['photo'])
            def handle_docs_document(message):
                print(user_id)
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = f"{PATH}/con/photo/service_check_image_id/{user_id}-{message.photo[1].file_id}.png"

                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                DATA_TRANSACTION['service_check_image_id'] = message.photo[1].file_id

                photo = open(src, 'rb')
                bot.send_photo(user_id, photo)
