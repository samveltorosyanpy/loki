import os
from con.classes.JsonDataTrans import JsonFunctions

path = os.path.dirname(__file__).split('/')[1:-2]

class DownloadFiles():
    def __init__(self, path):
        self.path = path

    def Photo_Download(self, bot, my_chat_id):
        @bot.message_handler(content_types=['photo'])
        def handle_docs_document(message):
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = f"{self.path}/con/photo/{message.photo[1].file_id}.png"
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            photo = open(src, 'rb')
            bot.send_photo(my_chat_id, photo)
            json_f = JsonFunctions(["user_check_image_id"],
                                   [str(message.photo[1].file_id)], self.path)
            json_f.Dump()