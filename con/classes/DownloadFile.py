import time
from con.classes.conf.configuration import *
from con.classes.SQL.tables.conf.config import *
from con.classes.buttons.button import ButtonsClass
from con.classes.SQL.tables.TransactionData import TransactionData
from con.classes.SQL.tables.Transactions import TransactionExchange


Transaction = TransactionExchange()
Photo = TransactionData()
Sessions = Session()


class DownloadFiles():
    def __init__(self):
        pass

    def Photo_Download(self, bot):
        @bot.message_handler(content_types=['photo'])
        def handle_docs_document(message):
            transaction_id = TransactionExchange().TransactionLastId(message.chat.id)
            state = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]
            if state == 'waiting_user_photo':
                time_msg = Translate().ShowText(message.chat.id, 39)
                sm = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]
                bot.send_message(message.chat.id, text=f"{time_msg} {sm[0]}")

                for id in range(1, len(sm)):
                    bot.edit_message_text(text=f"{time_msg} {sm[id]}", chat_id=message.chat.id,
                                          message_id=message.message_id + 1)
                    time.sleep(0.1)

                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = f"{PATH}/con/photo/client_check_image_id/{message.chat.id}-{message.photo[1].file_id}.png"

                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                TransactionData().InsertTransactionPhoto(time_interval=None, client_check_image_id=message.photo[1].file_id,
                                                         transaction_id=TransactionExchange().TransactionLastId(message.chat.id))

                Transaction.ValueUpdate({'state_transaction': "waiting_confirm_admin"},
                                        id=message.chat.id)


                admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                    TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

                bot.send_message(admin_id, text=Translate().ShowText(admin_id, 33))
                photo = open(src, 'rb')
                bot.send_photo(admin_id, photo, reply_markup=ButtonsClass().MarkupConfirm(message))

        # else:
        #     if DATA_TRANSACTION["client_check_image_id"] == None:
        #         print("nkar@ uxarkvac che useri koxmic")
        #
        #     elif DATA_TRANSACTION["client_check_image_id"] != None:
        #         print("user@ uxarkec nkar@")
        #
        #     else:
        #         print("cheq uzum transaqciai ktron@ uxarkeq")
