import random
from telebot import types
from datetime import datetime
from con.classes.conf.configuration import *
from con.classes.ApiRequests import ClassApis
from con.classes.DownloadFile import DownloadFiles
from con.classes.SQL.StartingPostgres import *


class Churancy_chack():
    def __init__(self):
        pass

    def CurChack(self, bot):

        @bot.message_handler(content_types=['text'])
        def changing_real_time(message):
            user_status = str(Sessions.query(TelegramUser.user_state).filter(TelegramUser.id == message.chat.id)[0][0])
            if user_status == "admin" or user_status == "owner_admin":
                try:
                    user_id = str(message.text).split('|')[1]
                    state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                        TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                            user_id))[0][0]
                    if state_transaction == "waiting_service_check_number":
                        blockchane_url = str(message.text).split('|')[0]
                        value = {"service_check_index": str(blockchane_url)}
                        TransactionPhoto().ValueUpdate(value=value, id=int(user_id))
                        TransactionExchange().ValueUpdate(value={'state_transaction': "success"}, id=user_id)
                except IndexError as ex:
                    pass

            else:
                amount_user = Sessions.query(TransactionExchange.amount_user).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(message.chat.id))[0][
                    0]
                curacy = Sessions.query(TransactionExchange.curacy).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(message.chat.id))[0][
                    0]
                cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]
                state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]
                type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]

                if amount_user == 0 and state_transaction == "waiting_user_amount":
                    while message.text.isnumeric():
                        amount_exchange = int(message.text)
                        while amount_exchange >= limits_amount_exchange[curacy]:

                            amount_user = message.text

                            Exchange = ClassApis([cryptocoin])
                            amount_crypto, amd_amount_pr = Exchange.crypto_price_user(curacy=curacy,
                                                                                      amount_user=amount_user)

                            update_value = {"amount_user": float(amount_user), "amount_crypto": float(amount_crypto),
                                            "amd_amount_pr": float(amd_amount_pr),
                                            "state_transaction": 'waiting_user_wallet'}

                            TransactionExchange().ValueUpdate(value=update_value,
                                                              id=message.chat.id)

                            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                                    message.chat.id))[0][0]

                            if type_transaction == "Buy":

                                markup_wallet = types.InlineKeyboardMarkup(row_width=2)
                                type_wallet1 = types.InlineKeyboardButton(text='Idram', callback_data="Idram")
                                type_wallet2 = types.InlineKeyboardButton(text='Telcell', callback_data='Telcell')
                                type_wallet3 = types.InlineKeyboardButton(text='Easypay', callback_data='Easypay')
                                type_wallet4 = types.InlineKeyboardButton(text='↩️back', callback_data='back_wallet')
                                markup_wallet.add(type_wallet1, type_wallet2, type_wallet3, type_wallet4)
                                bot.send_message(message.chat.id, text=SENTENCE_BOT[
                                    Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][
                                        0]][12],
                                                 reply_markup=markup_wallet)
                            elif type_transaction == "Sell":
                                bot.send_message(message.chat.id, f"""
    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][10][0]}
    
    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][10][2]} {amount_crypto} {cryptocoin}
    
    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][10][1]}
                                                    """, )
                                # {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][10][3]} {cryptocoin} {wallet_data[cryptocoin.upper()]['wallet_key']}
                                TransactionExchange().ValueUpdate(value={"state_transaction": "waiting_user_photo"},
                                                                  id=message.chat.id)

                                send_user_chack = DownloadFiles()
                                send_user_chack.Photo_Download(bot)

                            break

                        else:
                            bot.send_message(message.chat.id,
                                             f"{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][13]} {limits_amount_exchange[curacy]}")

                            break

                        break

                    else:
                        bot.send_message(message.chat.id, text=SENTENCE_BOT[
                            Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][14])

                elif state_transaction == "waiting_user_wallet_number" or state_transaction == "waiting_service_check_number":

                    TransactionExchange().ValueUpdate(
                        value={'user_wallet': message.text, "state_transaction": "waiting_service_check_number"},
                        id=message.chat.id)

                    admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

                    markup_send_blockchane = types.InlineKeyboardMarkup(row_width=2)

                    type_cour1 = types.InlineKeyboardButton(text='Send',
                                                            callback_data=f"SendBlockchaneUrl_{message.chat.id}")
                    type_cour2 = types.InlineKeyboardButton(text='Qcel :D', callback_data=f'failed_{message.chat.id}')

                    markup_send_blockchane.add(type_cour1, type_cour2)
                    if type_transaction == "Buy":
                        bot.send_message(admin_id, text=f"User id [{message.chat.id}] | uxarkeq blockchanei hxum@",
                                         reply_markup=markup_send_blockchane)
                    elif type_transaction == "Sell":
                        bot.send_message(admin_id, text=f"User id [{message.chat.id}] | uxarkeq ktroni hamar@",
                                         reply_markup=markup_send_blockchane)

                elif state_transaction == 'waiting_manual_time':
                    time = message.text
                    try:
                        time1 = bool(datetime.strptime(time.split('-')[0], "%H:%M").strftime("%H:%M"))
                        time2 = bool(datetime.strptime(time.split('-')[1], "%H:%M").strftime("%H:%M"))
                    except:
                        time1 = False
                        time2 = False
                    while time1 == True or time2 == True:
                        bot.send_message(message.chat.id, text="xndrum enq grel poxancvac gumari chaps@")
                        TransactionExchange().ValueUpdate(
                            value={"state_transaction": "waiting_manual_amount"},
                            id=message.chat.id)
                        TransactionIsNotPhoto().InsertTransactionChackInfo(
                            value={"time_interval": message.text},
                            user_id=message.chat.id)
                        break
                    else:
                        bot.send_message(message.chat.id, text="xndrum enq hetyevel nshvac formatin '20:00-20:30'")

                elif state_transaction == "waiting_manual_amount":

                    while message.text.isnumeric():

                        amount_exchange = int(message.text)

                        while amount_exchange >= limits_amount_exchange[curacy]:
                            TransactionPhoto().InsertTransactionPhoto(value={"client_check_image_id": None}, user_id=message.chat.id)
                            TransactionIsNotPhoto().ValueUpdate(value={"amount": message.text}, id=message.chat.id)

                            admins = list(Sessions.query(TelegramUser.id).filter(TelegramUser.user_state == "admin" or TelegramUser.user_state == "owner_admin"))
                            random_admin_id = random.choice(admins)[0]

                            time_interval = Sessions.query(TransactionIsNotPhoto.time_interval).filter(
                                TransactionIsNotPhoto.transaction_id == TransactionExchange().TransactionLastId(
                                    message.chat.id))[0][0]

                            Transaction.ValueUpdate(
                                value={"state_transaction": "waiting_confirm_admin", "admin_id": random_admin_id},
                                id=message.chat.id)

                            markup_send_for_user_chack_info = types.InlineKeyboardMarkup(row_width=2)
                            type_cour1 = types.InlineKeyboardButton(text='confirm',
                                                                    callback_data=f"SendPhotoUser_{message.chat.id}")
                            type_cour2 = types.InlineKeyboardButton(text='Cancel', callback_data='cancel_check')
                            markup_send_for_user_chack_info.add(type_cour1, type_cour2)

                            bot.send_message(random_admin_id,
                                             text=f"""amount-{message.text}
                                             time interval-{time_interval}""")

                            bot.send_message(random_admin_id,
                                             text="user@ chuni chek xndum enq stugel nshvac jamuv nshvac gumari qanakov ktron ka",
                                             reply_markup=markup_send_for_user_chack_info)

                            break

                        else:

                            bot.send_message(message.chat.id,
                                             f"{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][13]} {limits_amount_exchange[curacy]}")

                            break

                        break

                    else:

                        bot.send_message(message.chat.id, text=SENTENCE_BOT[
                            Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][14])
