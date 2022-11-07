import time
from datetime import datetime
from loguru import logger
from flask import Flask, request
from con.classes.Binance import BnanceApi
from con.classes.conf.configuration import *
from con.classes.ApiRequests import ClassApis
from con.classes.SQL.StartingPostgres import *
from con.classes.Utilites.Utils import UtilsApp
from con.classes.BigTextsClass import BuySellClass
from con.classes.buttons.button import ButtonsClass
from con.classes.SQL.tables.TranslateTable import Translate

# from con.classes.SQL.tables.Transactions import TransactionExchange

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start', 'clear', 'language', 'admin'])
def choose_transaction(message):
    if message.text == "/clear":
        # clear kanchelu depqum maqrvum e sax informatian transaciayi het kapvac
        delete_information = UtilsApp(bot=bot, message=message)
        delete_information.DelleteTransactionData(message.chat.id)

        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 5))

    if message.text == "/start":
        bot.send_message(message.chat.id, "s")
        # transacian sksvum e estexic user@ @ntrum e kriptovalutai tesak@ vor@ cankanum e poxanakel fyucherov
        username = message.from_user.username if message.from_user.username is not None else message.from_user.last_name

        UserTable.InsertUser(id=int(message.chat.id), user_name=str(username), language="russian",
                             user_state="client")

        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 1),
                         reply_markup=ButtonsClass().MarkupStart(message))

    if message.text == "/language":
        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 3),
                         reply_markup=ButtonsClass().MarkupLanguage())

    if message.text == "/admin" and message.chat.id == owner_id:
        pass


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    Chack = UtilsApp(bot, call.message)

    if call.data == "dash":

        try:
            state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]
        except IndexError as ex:
            state_transaction = None

        if state_transaction in static_status:

            random_operatr = UtilsApp(bot, call.message).RandomAdmins()

            Transaction.InsertTransactionPending(cryptocoin=call.data, state_transaction=state_transaction,
                                                 user_id=call.message.chat.id, admin_id=random_operatr)

            bot.send_message(call.message.chat.id, text=Translate().ShowText(call.message.chat.id, 8),
                             reply_markup=ButtonsClass().MarkupBuySell(call.message, call.data))

        else:
            Chack.ChackState(state_transaction)

    elif call.data == "btc" or call.data == "usdt" or call.data == "xrp":
        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

        if state_transaction in static_status:
            bot.send_message(call.message.chat.id,
                             text=f"{Translate().ShowText(call.message.chat.id, 40)} /start")
        else:
            Chack.ChackState(state_transaction)

    elif str(call.data).split("|")[0] == "Buy" or str(call.data).split("|")[0] == "Sell":

        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

        if state_transaction in static_status:

            cryptocoin = str(call.data).split("|")[1]

            Transaction.ValueUpdate(value={'type_transaction': str(call.data).split('|')[0],
                                           "state_transaction": "waiting_user_carncy"}, id=call.message.chat.id)

            bot.send_message(call.message.chat.id, text=Translate().ShowText(call.message.chat.id, 41),
                             reply_markup=ButtonsClass().MarkupReadAmount(cryptocoin))

            # bot.send_message(call.message.chat.id, text=Translate().ShowText(call.message.chat.id, 41))
        else:
            Chack.ChackState(state_transaction)

    elif call.data in curacy_array:

        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

        if state_transaction in static_status:

            Transaction.ValueUpdate(value={"state_transaction": "waiting_user_amount",
                                           "curacy": str(call.data).split('_')[1].upper()},
                                    id=call.message.chat.id)
# pr_read
#             bot.send_message(chat_id=call.message.chat.id, text=f"""
# {Translate().ShowText(call.message.chat.id, 11)}
#
# {Translate().ShowText(call.message.chat.id, 53)}
# """,
#                              reply_markup=ButtonsClass().MarkupRead(Translate().ShowText(call.message.chat.id, 50)), )

            bot.send_message(chat_id=call.message.chat.id, text=f"{Translate().ShowText(call.message.chat.id, 11)}")

        else:
            Chack.ChackState(state_transaction)

# pr_read
#     elif call.data == "read_rp":
#
#         state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
#             TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]
#
#         pr_read = Sessions.query(TransactionExchange.pr_read).filter(
#             TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[
#             0][0]
#
#         if state_transaction == "waiting_user_amount":
#
#             if pr_read is True:
#                 Burron_text = Translate().ShowText(call.message.chat.id, 50)
#                 bool_pr = False
#
#                 pr_text = f"""
# {Translate().ShowText(call.message.chat.id, 11)}
#
# {Translate().ShowText(call.message.chat.id, 53)}
#                     """
#
#             if pr_read is False:
#                 Burron_text = Translate().ShowText(call.message.chat.id, 49)
#                 bool_pr = True
#                 pr_text = f"""
# {Translate().ShowText(call.message.chat.id, 11)}
#
# {Translate().ShowText(call.message.chat.id, 54)}
#                     """
#
#             Transaction.ValueUpdate(value={"pr_read": bool_pr}, id=call.message.chat.id)
#
#             bot.edit_message_text(text=pr_text, message_id=call.message.message_id, chat_id=call.message.chat.id,
#                                   reply_markup=ButtonsClass().MarkupRead(Burron_text))
#         else:
#             Chack.ChackState(state_transaction)

    elif call.data == "Idram" or call.data == "Telcell" or call.data == "Easypay":

        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

        if state_transaction == f'waiting_user_wallet' or state_transaction == f'waiting_choose_wallet':

            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

            Transaction.ValueUpdate(value={"armenian_wallet": str(call.data)}, id=call.message.chat.id)

            if type_transaction == "Buy":

                Transaction.ValueUpdate(value={"state_transaction": "waiting_user_photo", },
                                        id=call.message.chat.id)

                BuySellClass(call.message.chat.id, type_transaction, bot).InformationSendMany(call.message)

            elif type_transaction == "Sell":

                bot.send_message(call.message.chat.id,
                                 text=F"{Translate().ShowText(call.message.chat.id, 17)} {call.data} {Translate().ShowText(call.message.chat.id, 18)}")

                Transaction.ValueUpdate(value={'state_transaction': 'waiting_user_wallet_number'},
                                        id=call.message.chat.id)

                Sessions.query(TransactionExchange).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        call.message.chat.id))

        else:
            Chack.ChackState(state_transaction)

    elif str(call.data).split("|")[0] == "confirm":

        user_id = str(call.data).split("|")[1]
        transaction_id = Transaction.TransactionLastId(user_id)

        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]

        if state_transaction == "waiting_confirm_admin":

            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]

            if type_transaction == "Buy":

                cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                    TransactionExchange.transaction_id == transaction_id)[0][0]

                bot.send_message(int(user_id),
                                 text=f"{Translate().ShowText(int(user_id), 17)} {cryptocoin} {Translate().ShowText(int(user_id), 18)}")

                Transaction.ValueUpdate(value={'state_transaction': 'waiting_user_wallet_number'},
                                        id=int(user_id))

            elif type_transaction == "Sell":

                bot.send_message(user_id,
                                 text=f"{Translate().ShowText(call.message.chat.id, 19)}",
                                 reply_markup=ButtonsClass().MarkupChoosWallet())

                Transaction.ValueUpdate(value={'state_transaction': 'waiting_choose_wallet'}, id=user_id)

    elif call.data == "manually":

        transaction_id = Transaction.TransactionLastId(call.message.chat.id)
        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]

        if state_transaction == "waiting_user_photo":

            Transaction.ValueUpdate(value={"state_transaction": 'waiting_manual_time'},
                                    id=call.message.chat.id)
            bot.send_message(call.message.chat.id,
                             text=f"{Translate().ShowText(call.message.chat.id, 28)} '20:00-20:30'")



        else:
            Chack.ChackState(state_transaction)

    elif str(call.data).split('|')[0] == "send_crypto":
        user_id = str(call.data).split('|')[1]
        transaction_id = Transaction.TransactionLastId(user_id)
        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]

        if state_transaction == "waiting_service_check_number":

            user_wallet = Sessions.query(TransactionExchange.user_wallet).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                    user_id))[0][0]
            amount_crypto_pr = Sessions.query(TransactionExchange.amount_crypto_pr).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                    user_id))[0][0]
            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                    user_id))[0][0]
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                    user_id))[0][0]

            description = f"transaction_id  &{TransactionExchange().TransactionLastId(user_id)}  user_id  &{user_id}"

            SendCryptoClass = BnanceApi(bot=bot, message=call.message)

            trx_id = SendCryptoClass.SendCrypto(crypto=str(cryptocoin).lower(), user_address=str(user_wallet),
                                           amount=float(amount_crypto_pr),
                                           description=description, user_id=user_id)

            # TransactionData().ValueUpdate(value={"service_check_index": trx_id}, id=user_id)
            TransactionExchange().ValueUpdate(value={'state_transaction': "success"}, id=user_id)

            ch = BuySellClass(user_id, type_transaction, bot)
            bot.send_message(user_id, text=ch.Cack())

        else:
            Chack.ChackState(state_transaction)

    elif str(call.data).split('_')[0] == "CancelCheck":
        user_id = str(call.data).split('_')[1]
        transaction_id = Transaction.TransactionLastId(user_id)

        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]

        if state_transaction == "waiting_confirm_admin" and type_transaction == "Buy":
            bot.send_message(user_id, text=Translate().ShowText(user_id, 27))
            Transaction.ValueUpdate({'state_transaction': "waiting_user_photo"}, id=user_id)

        if state_transaction == "waiting_confirm_admin" and type_transaction == "Sell":
            bot.send_message(user_id, text=Translate().ShowText(user_id, 52))
            Transaction.ValueUpdate({'state_transaction': "waiting_user_send_id"}, id=user_id)

        else:
            Chack.ChackState(state_transaction)

    elif call.data == "ShowPrice":

        AllPrice = ClassApis(cryptocoin_array)
        all_price = AllPrice.all_crypto_price()

        bot.reply_to(call.message, text=f"""
{Translate().ShowText(call.message.chat.id, 9)}

✅  BTC/USD    {all_price[0]}
✅  XRP/USD    {all_price[1]}
✅  USDT/USD    {all_price[2]}
✅  DASH/USD   {all_price[3]}

{Translate().ShowText(call.message.chat.id, 10)}
        """)
        logger.debug(
            f"""user {call.message.chat.id} click the ShowPrice"""
        )

    elif call.data == "armenian_language" or call.data == 'russian_language' or call.data == 'english_language':

        language = str(call.data).split("_")[0]
        Sessions.query(TelegramUser).filter(TelegramUser.id == call.message.chat.id).update(
            values={"language": language})

        Sessions.commit()
        Sessions.close()

        bot.send_message(call.message.chat.id, text=Translate().ShowText(call.message.chat.id, 24))
        logger.debug(f"User id [{call.message.chat.id}] | Update the language [{language.upper()}]")

    else:
        pass


@bot.message_handler(content_types=['text'])
def changing_real_time(message):
    user_status = str(Sessions.query(TelegramUser.user_state).filter(TelegramUser.id == message.chat.id)[0][0])

    if user_status == "admin" or user_status == "owner_admin":

        try:

            user_id = int(str(message.text).split('|')[0])

            state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                    user_id))[0][0]
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                    user_id))[0][0]

            if state_transaction == "waiting_service_check_number" and type_transaction == "Sell":
                trx_id = str(message.text).split("|")[1]

                TransactionData().ValueUpdate(value={"service_check_index": trx_id},
                                              id=int(user_id))
                TransactionExchange().ValueUpdate(value={'state_transaction': "success"}, id=user_id)

                ch = BuySellClass(user_id, type_transaction, bot)
                bot.send_message(user_id, text=ch.Cack())
            elif state_transaction == "waiting_service_check_number" and type_transaction == "Buy":
                trx_id = str(message.text).split("|")[1]

                TransactionData().ValueUpdate(value={"service_check_index": trx_id}, id=int(user_id))

        except IndexError as ex:
            pass

    else:

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
        pr_read = Sessions.query(TransactionExchange.pr_read).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                message.chat.id))[0][0]

        if state_transaction == "waiting_user_amount":

            try:
                float(message.text)
                slt = True
            except ValueError:
                slt = False

            while slt == True:

                amount_exchange = float(message.text)

                while amount_exchange >= min_limits_amount_exchange[curacy] and amount_exchange <= \
                        max_limits_amount_exchange[curacy]:

                    amount_user = message.text
                    # Exchange.crypto_price_user(message=message)

                    Exchange = ClassApis([cryptocoin])
                    amd_amount_pr, amount_crypto_pr, amount_crypto = 1, 1, 1

                    type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                        TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                            message.chat.id))[0][0]

                    update_value = {
                        "amount_user": float(amount_user),
                        "amount_crypto": float(amount_crypto),
                        "amd_amount_pr": float(amd_amount_pr),
                        "amount_crypto_pr": float(amount_crypto_pr),
                        "state_transaction": f'waiting_user_wallet',
                        'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                    TransactionExchange().ValueUpdate(value=update_value, id=message.chat.id)

                    if type_transaction == "Buy":

                        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 19),
                                         reply_markup=ButtonsClass().MarkupChoosWallet())

                    elif type_transaction == "Sell":
                        owner_wallet = BnanceApi(bot=bot, message=message).address

                        Transaction.ValueUpdate(
                            value={"state_transaction": "waiting_user_send_id", "owner_wallet": owner_wallet},
                            id=message.chat.id)

                        crypto_check = BuySellClass(message.chat.id, "Sell", bot)
                        crypto_check.InformationSendMany(message)

                    break

                else:
                    bot.send_message(message.chat.id,
                                     f"{Translate().ShowText(message.chat.id, 20)} {min_limits_amount_exchange[curacy]} {Translate().ShowText(message.chat.id, 34)} {max_limits_amount_exchange[curacy]}")

                    break

                break


            else:
                bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 21))

        elif state_transaction == "waiting_user_send_id":

            Transaction.ValueUpdate({'state_transaction': "waiting_confirm_admin"},
                                    id=message.chat.id)
            TransactionData().InsertTransactionPhoto(time_interval=None, client_check_image_id=message.text,
                                                     transaction_id=Transaction.TransactionLastId(message.chat.id))

            admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

            bot.send_message(admin_id, text=f"URL: {message.text}")
            bot.send_message(admin_id, text=Translate().ShowText(admin_id, 33),
                             reply_markup=ButtonsClass().MarkupConfirm(message))

        if state_transaction == "waiting_user_wallet_number":

            TransactionExchange().ValueUpdate(
                value={'user_wallet': message.text, "state_transaction": "waiting_service_check_number"},
                id=message.chat.id)

            trans_id = TransactionExchange().TransactionLastId(message.chat.id)
            admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
            user_wallet = Sessions.query(TransactionExchange.user_wallet).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
            armenian_wallet = Sessions.query(TransactionExchange.armenian_wallet).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
            amount = Sessions.query(TransactionExchange.amount_crypto_pr).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
            amd_amount_pr = Sessions.query(TransactionExchange.amd_amount_pr).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
            curacy = Sessions.query(TransactionExchange.curacy).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]

            if type_transaction == "Buy":

                bot.send_message(admin_id, text=f"""
User id  &`{message.chat.id}`    &`{trans_id}`
Crypto   Amount   {cryptocoin}   `{amount}`
Address      `{message.text}`
                        """, parse_mode='MarkdownV2')

                bot.send_message(admin_id, text=Translate().ShowText(admin_id, 35),
                                 reply_markup=ButtonsClass().MarkupSend(message))

            elif type_transaction == "Sell":

                bot.send_message(admin_id, text=f"|{message.chat.id}")
                bot.send_message(admin_id, text=f"""
{Translate().ShowText(admin_id, 36)} {user_wallet} {armenian_wallet}
{amd_amount_pr} {curacy}
{Translate().ShowText(admin_id, 35)}
    """,
                                 )

        elif state_transaction == 'waiting_manual_time':

            time_s = message.text

            try:

                time1 = bool(datetime.strptime(time_s.split('-')[0], "%H:%M").strftime("%H:%M"))
                time2 = bool(datetime.strptime(time_s.split('-')[1], "%H:%M").strftime("%H:%M"))

            except:

                time1 = False
                time2 = False

            while time1 == True or time2 == True:

                bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 29))

                TransactionExchange().ValueUpdate(
                    value={"state_transaction": "waiting_manual_amount"},
                    id=message.chat.id)

                transaction_id = TransactionExchange().TransactionLastId(message.chat.id)
                TransactionData().InsertTransactionPhoto(time_interval=message.text, client_check_image_id=None,
                                                         transaction_id=int(transaction_id))

                break

            else:

                bot.send_message(message.chat.id,
                                 text=F"{Translate().ShowText(message.chat.id, 30)} '20:00-20:30'")

        elif state_transaction == "waiting_manual_amount":

            try:
                float(message.text)
                slt = True
            except ValueError:
                slt = False

            while slt == True:

                amount_exchange = float(message.text)

                while amount_exchange >= min_limits_amount_exchange["AMD"] and amount_exchange <= \
                        max_limits_amount_exchange["AMD"]:

                    time_interval = Sessions.query(TransactionData.time_interval).filter(
                        TransactionData.transaction_id == TransactionExchange().TransactionLastId(
                            message.chat.id))[0][0]

                    TransactionData().ValueUpdate(value={"amount": message.text}, id=message.chat.id)

                    Transaction.ValueUpdate(
                        value={"state_transaction": "waiting_confirm_admin"},
                        id=message.chat.id)

                    admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[
                        0][0]

                    bot.send_message(admin_id, text=f"""
    amount-{message.text}
    time interval-{time_interval}
    """)
                    bot.send_message(admin_id, text=Translate().ShowText(admin_id, 31),
                                     reply_markup=ButtonsClass().MarkupConfirm(message))

                    break

                else:

                    bot.send_message(message.chat.id,
                                     f"{Translate().ShowText(message.chat.id, 20)} {min_limits_amount_exchange['AMD']} {Translate().ShowText(message.chat.id, 34)} {max_limits_amount_exchange['AMD']}")

                    break

                break

            else:

                bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 21))


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
                                                 transaction_id=TransactionExchange().TransactionLastId(
                                                     message.chat.id))

        Transaction.ValueUpdate({'state_transaction': "waiting_confirm_admin"},
                                id=message.chat.id)

        admin_id = Sessions.query(TransactionExchange.admin_id).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

        bot.send_message(admin_id, text=Translate().ShowText(admin_id, 33))
        photo = open(src, 'rb')
        bot.send_photo(admin_id, photo, reply_markup=ButtonsClass().MarkupConfirm(message))


# @server.route('/' + TOKEN, methods=['POST'])
# def getMessage():
#     json_string = request.get_data().decode('utf-8')
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200
#
#
# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://loki.samveltorosyan90.workers.dev/' + str(TOKEN))
#     return "!", 200
#
#
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    # print(os.system("dig +short myip.opendns.com @resolver1.opendns.com"))
    bot.delete_webhook()
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "start the bot"),
        telebot.types.BotCommand("/language", "choose a language"),
        telebot.types.BotCommand("/clear", "mqrel texekutyun@"),
    ])
    bot.polling(none_stop=True, interval=0)

# db-ic select linox informacian texapoxvi arandin config faili mech
# serveri anjatvel mianaluc heto transaqcian petqa sharunakvi
# imanal te inchpes petqa anjatvi knopkeqi lselu mod@

# logeri garc@ lucel json faili ognutyamb
# texteri het xnirner@ lucel

# admin panel@
# botum avelacnel admin funkcian
# interfaceum tal hnaravorutyun user id-ov poxel useri status@
