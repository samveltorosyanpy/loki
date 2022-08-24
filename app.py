import telebot
from telebot import types
from loguru import logger
from datetime import datetime
from flask import Flask, request
from con.classes.conf.configuration import *
from con.classes.SQL.StartingPostgres import *
from con.classes.ApiRequests import ClassApis
from con.classes.DownloadFile import DownloadFiles
from con.classes.CuracyChack import Churancy_chack

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


def start_bot(bot):
    @bot.message_handler(commands=['start', 'clear', 'language', 'admin'])
    def choose_transaction(message):
        if message.text == "/clear":
            Sessions.query(TransactionExchange).filter(
                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(message.chat.id)).delete()
            Sessions.commit()
            bot.send_message(message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][4])

        if message.text == "/start":
            # logger.add(f"{PATH}/con/logs/{message.chat.id}_user_log.log", format="{time}, {level}, {message}",
            #            level="DEBUG")
            username = message.from_user.username if message.from_user.username is not None else message.from_user.last_name
            UserTable.InsertUser(id=message.chat.id, user_name=username, language="russian", user_state="client")

            markup = types.InlineKeyboardMarkup(row_width=2)
            type_cour1 = types.InlineKeyboardButton(text='BTC', callback_data="btc")
            type_cour2 = types.InlineKeyboardButton(text='DASH', callback_data='dash')
            type_cour3 = types.InlineKeyboardButton(text='LTC', callback_data='ltc')
            type_cour4 = types.InlineKeyboardButton(text='XRP', callback_data='xrp')
            type_cour5 = types.InlineKeyboardButton(text=SENTENCE_BOT[
                Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][1],
                                                    callback_data='ShowPrice')
            markup.add(type_cour1, type_cour2, type_cour3, type_cour4, type_cour5)
            bot.send_message(message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][0],
                             reply_markup=markup)

        if message.text == "/language":
            markup_language = types.InlineKeyboardMarkup(row_width=1)
            type_language1 = types.InlineKeyboardButton(text='🇦🇲 Հայերեն', callback_data="armenian_language")
            type_language2 = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian_language')
            type_language3 = types.InlineKeyboardButton(text='🇬🇧 English', callback_data='english_language')

            markup_language.add(type_language1, type_language2, type_language3)
            bot.send_message(message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == message.chat.id)[0][0]][2],
                             reply_markup=markup_language)
            logger.debug(F"""User [{message.chat.id}] poxec ir ogtagorcman lezun""")

        if message.text == "/admin":
            bot.send_message(message.chat.id, text="""
            barev, du mutq es gorcel boti admin hartak vortex karox es boti het kapvac kargavorumner anel""")

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        if call.data == "btc" or call.data == "dash" or call.data == "ltc" or call.data == "xrp":
            Transaction.InsertTransactionPending(cryptocoin=call.data, user_id=call.message.chat.id)

            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

            markup_buy_sell = types.InlineKeyboardMarkup(row_width=2)
            type_buy = types.InlineKeyboardButton(text=str(SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(
                TelegramUser.id == call.message.chat.id)[0][0]][5]),
                                                  callback_data=f"Buy {cryptocoin}")
            type_sell = types.InlineKeyboardButton(text=str(SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(
                TelegramUser.id == call.message.chat.id)[0][0]][6]),
                                                   callback_data=f"Sell {cryptocoin}")
            markup_buy_sell.add(type_buy, type_sell)
            bot.send_message(call.message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][
                7],
                             reply_markup=markup_buy_sell)
            logger.debug(f"""Insert transaction cryptocoin={call.data}, user_id={call.message.chat.id}.""")
            logger.debug(f"User {call.message.chat.id} click {str(call.data)}")

        elif call.data == "ShowPrice":
            cryptocoin_array = ['BTC', 'XRP', 'LTC', 'DASH']
            AllPrice = ClassApis(cryptocoin_array)
            all_price = AllPrice.all_crypto_price()
            bot.reply_to(call.message, text=f"""
{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][8][0]}

✅  BTC/USD    {all_price[0]}
✅  XRP/USD    {all_price[1]}
✅  LTC/USD    {all_price[2]}
✅  DASH/USD   {all_price[3]}

{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][8][1]}""")
            logger.debug(
                f"""user {call.message.chat.id} click the ShowPrice"""
            )

        elif call.data == "armenian_language" or call.data == 'russian_language' or call.data == 'english_language':
            language = str(call.data).split("_")[0]
            Sessions.query(TelegramUser).filter(TelegramUser.id == call.message.chat.id).update(
                values={"language": language})
            Sessions.commit()
            Sessions.close()
            bot.send_message(call.message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][
                17])
            logger.debug(f"User id [{call.message.chat.id}] | Update the language [{language.upper()}]")

        elif str(call.data).split(' ')[0] == "Buy" or str(call.data).split(' ')[0] == "Sell":

            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]
            Transaction.ValueUpdate(value={'type_transaction': str(call.data).split(' ')[0]},
                                    id=call.message.chat.id)

            markup_curacy = types.InlineKeyboardMarkup(row_width=3)
            curacy1 = types.InlineKeyboardButton(text=f"AMD", callback_data=f"to_amd")
            curacy2 = types.InlineKeyboardButton(text=f"USD", callback_data=f"to_usd")
            curacy3 = types.InlineKeyboardButton(text=f"{cryptocoin.upper()}", callback_data=f"to_{cryptocoin.lower()}")
            markup_curacy.add(curacy1, curacy2, curacy3)
            bot.send_message(call.message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][
                3], reply_markup=markup_curacy)

        elif call.data == f"to_btc" or call.data == f"to_xrp" or call.data == f"to_ltc" or call.data == f"to_dash" or call.data == "to_amd" or call.data == "to_usd" or call.data == "back_wallet":
            if call.data == "back_wallet":
                Transaction.ValueUpdate(value={"amount_user": 0}, id=call.message.chat.id)
            else:
                Transaction.ValueUpdate(value={"amount_user": 0, "state_transaction": "waiting_user_amount",
                                               "curacy": str(call.data).split('_')[1].upper()}, id=call.message.chat.id)

            bot.send_message(call.message.chat.id, text=
            SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][
                9])

            ClassMCH = Churancy_chack()
            ClassMCH.CurChack(bot)


        elif call.data == "Idram" or call.data == "Telcell" or call.data == "Easypay":

            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]
            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]
            amount_crypto = Sessions.query(TransactionExchange.amount_crypto).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]
            amd_amount_pr = (Sessions.query(TransactionExchange.amd_amount_pr).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0])
            state = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(call.message.chat.id))[0][0]

            Transaction.ValueUpdate(value={"armenian_wallet": str(call.data)},
                                    id=call.message.chat.id)

            if type_transaction == "Buy":
                Transaction.ValueUpdate(value={"state_transaction": "waiting_user_photo", }, id=call.message.chat.id)

                bot.send_message(call.message.chat.id, f"""
    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][10][0]}

    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][10][2]} {float(amount_crypto)} {cryptocoin}
    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][10][4]} {amd_amount_pr} AMD


    {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][10][1]}
    """, )

                markup_manually = types.InlineKeyboardMarkup(row_width=1)
                manual = types.InlineKeyboardButton(text=SENTENCE_BOT[
                    Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][19],
                                                    callback_data="manually")
                markup_manually.add(manual)
                bot.send_message(call.message.chat.id, text="ete chuneq ktron apa sexmeq lracnel knopken",
                                 reply_markup=markup_manually)

                send_user_chack = DownloadFiles()
                send_user_chack.Photo_Download(bot)

            elif type_transaction == "Sell" and state == "waiting_choose_wallet":
                bot.send_message(call.message.chat.id,
                                 text=F"{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][11][0]} {call.data} {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == call.message.chat.id)[0][0]][11][1]}")
                Transaction.ValueUpdate(value={'state_transaction': 'waiting_user_wallet_number', },
                                        id=call.message.chat.id)
                Sessions.query(TransactionExchange).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(call.message.chat.id))

                ClassMCH = Churancy_chack()
                ClassMCH.CurChack(bot)

        elif str(call.data).split("_")[0] == "SendPhotoUser":
            transaction_id = Transaction.TransactionLastId(str(call.data).split("_")[1])
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]
            user_id = Sessions.query(TransactionExchange.user_id).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]

            if type_transaction == "Buy":

                cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                    TransactionExchange.transaction_id == transaction_id)[0][0]
                bot.send_message(int(user_id),
                                 text=f"{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == user_id)[0][0]][11][0]} {cryptocoin} {SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == user_id)[0][0]][11][1]}")
                Transaction.ValueUpdate(value={'state_transaction': 'waiting_user_wallet_number', },
                                        id=int(user_id))
                ClassMCH = Churancy_chack()
                ClassMCH.CurChack(bot)

            elif type_transaction == "Sell":
                markup_wallet = types.InlineKeyboardMarkup(row_width=2)
                type_wallet1 = types.InlineKeyboardButton(text='Idram', callback_data="Idram")
                type_wallet2 = types.InlineKeyboardButton(text='Telcell', callback_data='Telcell')
                type_wallet3 = types.InlineKeyboardButton(text='Easypay', callback_data='Easypay')
                markup_wallet.add(type_wallet1, type_wallet2, type_wallet3)
                bot.send_message(user_id,
                                 text=f"{SENTENCE_BOT[Sessions.query(TelegramUser.language).filter(TelegramUser.id == user_id)[0][0]][12]}",
                                 reply_markup=markup_wallet)
                Transaction.ValueUpdate(value={'state_transaction': 'waiting_choose_wallet', }, id=user_id)
                ClassMCH = Churancy_chack()
                ClassMCH.CurChack(bot)

        elif str(call.data).split('_')[0] == "CancelCheck":
            user_id = str(call.data).split('_')[1]
            bot.send_message(user_id, text="xndrum enq noric uxarkel nkar@ aveli lav rakursic")
            Transaction.ValueUpdate({'state_transaction': "waiting_user_photo"}, id=user_id)

        elif call.data == "manually":
            Transaction.ValueUpdate(value={"state_transaction": 'waiting_manual_time'}, id=call.message.chat.id)
            bot.send_message(call.message.chat.id,
                             text="kxndrem grel motavor jam@ qnisin e katarvel poxancum@ partadir ays formatov '20:00-20:30'")
            ClassMCH = Churancy_chack()
            ClassMCH.CurChack(bot)


        elif str(call.data).split("_")[0] == "SendBlockchaneUrl":
            user_id = str(call.data).split("_")[1]
            transaction_id = Transaction.TransactionLastId(user_id)
            service_check_index = Sessions.query(TransactionPhoto.service_check_index).filter(
                TransactionPhoto.transaction_id == transaction_id)[0][0]
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]
            amd_amount_pr = Sessions.query(TransactionExchange.amd_amount_pr).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]
            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]
            user_wallet = Sessions.query(TransactionExchange.user_wallet).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]
            amount_crypto = Sessions.query(TransactionExchange.amount_crypto).filter(
                TransactionExchange.transaction_id == transaction_id)[0][0]

            bot.send_message(user_id, text=f"""
Գործարք № {transaction_id} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

գումարի չափը:  {int(amd_amount_pr)} AMD
Գործարքի տեսակ:  {type_transaction}
գումարի չափը կրիպտոարժույթով:
{amount_crypto} {cryptocoin}
{cryptocoin} Հաշվեհամար:
{user_wallet}
Փոխանցման URL հասցե:
{service_check_index}
""")


@server.route('/' + str(TOKEN), methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    start_bot(bot)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "start the bot"),
        telebot.types.BotCommand("/language", "choose a language"),
        telebot.types.BotCommand("/clear", "mqrel texekutyun@"),
    ])

# 30 rope heto chek@ atmena lini
# logeri garc@ lucel json faili ognutyamb
# texteri het xnirner@ lucel
# maximal gumar@ grelu qanak@ sahmanel ev data sarqel
# env fail@ havaqel
# admin panel@
# informacian poxelu hnaravorutyun
# sarqel database vortex grvum e informacia vor@ etaka klini popoxutyan boti ognutyamb
# botum avelacnel admin funkcian
# usernerin startus talu hnaravorutyun
# interfaceum tal hnaravorutyun user id-ov poxel useri status@


# if __name__ == '__main__':
#     bot = telebot.TeleBot(TOKEN)
#     start_bot(bot)
#     bot.set_my_commands([
#         telebot.types.BotCommand("/start", "start the bot"),
#         telebot.types.BotCommand("/language", "choose a language"),
#         telebot.types.BotCommand("/clear", "mqrel texekutyun@"),
#     ])
#     bot.polling(none_stop=True, interval=0)
