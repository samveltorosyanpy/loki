from telebot import types
from con.classes.conf.configuration import *
from con.classes.Utils import UtilsApp
from con.classes.SQL.tables.Transactions import TransactionExchange
from con.classes.SQL.tables.TransactionPhotos import TransactionPhoto
from con.classes.SQL.tables.Users import TelegramUser
from con.classes.SQL.tables.conf.config import *

Transaction = TransactionExchange()
Photo = TransactionPhoto()
Sessions = Session()


class DownloadFiles():
    def __init__(self):
        pass

    def Photo_Download(self, bot):
        @bot.message_handler(content_types=['photo'])
        def handle_docs_document(message):
            state = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(message.chat.id))[0][0]
            if state == 'waiting_user_photo':
                UtilsApp(bot, message).WaitingAdmin(message.chat.id)
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = f"{PATH}/con/photo/client_check_image_id/{message.chat.id}-{message.photo[1].file_id}.png"

                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)


                admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                    TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

                TransactionPhoto().InsertTransactionPhoto(value={'client_check_image_id': message.photo[1].file_id},
                                                          user_id=message.chat.id)
                Transaction.ValueUpdate({'state_transaction': "waiting_confirm_admin"},
                                        id=message.chat.id)

                markup_send_for_user_photo = types.InlineKeyboardMarkup(row_width=2)
                type_cour1 = types.InlineKeyboardButton(text='confirm',
                                                        callback_data=f"SendPhotoUser_{message.chat.id}")
                type_cour2 = types.InlineKeyboardButton(text='Cancel', callback_data=f'CancelCheck_{message.chat.id}')
                markup_send_for_user_photo.add(type_cour1, type_cour2)

                bot.send_message(admin_id, text=Translate().ShowText(admin_id, 33))
                photo = open(src, 'rb')
                bot.send_photo(admin_id, photo, reply_markup=markup_send_for_user_photo)

        # else:
        #     if DATA_TRANSACTION["client_check_image_id"] == None:
        #         print("nkar@ uxarkvac che useri koxmic")
        #
        #     elif DATA_TRANSACTION["client_check_image_id"] != None:
        #         print("user@ uxarkec nkar@")
        #
        #     else:
        #         print("cheq uzum transaqciai ktron@ uxarkeq")
