import telebot
from  datetime import datetime
from telebot import types
from con.configuration import *
from con.classes.api.ApiRequests import ClassApis
import admin

wallet_data = {
    'BTC': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'DASH': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'LTC': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'XRP': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'idram': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'telsel': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'easypay': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
}

def start_bot(bot):
    @bot.message_handler(commands=['start', 'close', 'admin', 'language'])
    def choose_transaction(message):
        if message.text == "/start":
            markup = types.InlineKeyboardMarkup(row_width=2)
            type_cour1 = types.InlineKeyboardButton(text='BTC', callback_data="btc")
            type_cour2 = types.InlineKeyboardButton(text='DASH', callback_data='dash')
            type_cour3 = types.InlineKeyboardButton(text='LTC', callback_data='ltc')
            type_cour4 = types.InlineKeyboardButton(text='XRP', callback_data='xrp')
            type_cour5 = types.InlineKeyboardButton(text='📈 Տեսնել կրիպտոների արժույթը', callback_data='ShowPrice')
            markup.add(type_cour1, type_cour2, type_cour3, type_cour4, type_cour5)
            DATA_TRANSACTION['username'] = message.from_user.username
            DATA_TRANSACTION['user_id'] = message.from_user.id
            bot.send_message(message.chat.id, text="Ընտրել կրիպտոարժույթը", reply_markup=markup)
        elif message.text == "/close":
            pass

        elif message.text == "/language":
            pass

        if message.chat.id == 1357108258 and message.text == "/admin":
            bot.send_message(message.chat.id, "write a user id ...")
            test_admin = admin.Administrator()
            test_admin.log_id(bot)



    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        if call.data == "btc" or call.data == "dash" or call.data == "ltc" or call.data == "xrp":
            DATA_TRANSACTION['cryptocoin'] = str(call.data)
            cryptocoin = DATA_TRANSACTION['cryptocoin']
            markup_buy_sell = types.InlineKeyboardMarkup(row_width=1)
            type_buy = types.InlineKeyboardButton(text=f"Գնել {cryptocoin}", callback_data=f"Buy {cryptocoin}")
            type_sell = types.InlineKeyboardButton(text=f"Վաճառել {cryptocoin}", callback_data=f"Sell {cryptocoin}")
            markup_buy_sell.add(type_buy, type_sell)
            bot.send_message(call.message.chat.id, text='Ընտրեք գործարքի տեսակը',
                             reply_markup=markup_buy_sell)

        elif call.data == "ShowPrice":
            cryptocoin_all = ['btc', 'xrp', 'ltc', 'dash']
            AllPrice = ClassApis(curacy=None, count=None, cryptocoin_array=cryptocoin_all)
            all_price = AllPrice.cripto_price()
            bot.reply_to(call.message, text=f"""
ays orva criptoarjuytneri gin@ boti nersum

✅ BTS    {all_price[0]}    USD
✅ BTS    {all_price[1]}    USD
✅ BTS    {all_price[2]}    USD
✅ BTS    {all_price[3]}    USD

ushadrutyun gin@ karoxx e chnchin tarberutyun tal
serveri taracutyan patcharov
""")

        elif call.data[:4] == "Buy " or call.data[:4] == "Sell":
            DATA_TRANSACTION['type_transaction'] = str(call.data).split(' ')[0]

            markup_curacy = types.InlineKeyboardMarkup(row_width=3)
            curacy1 = types.InlineKeyboardButton(text=f"AMD", callback_data=f"to_amd")
            curacy2 = types.InlineKeyboardButton(text=f"USD", callback_data=f"to_usd")
            curacy3 = types.InlineKeyboardButton(text=f"BTC", callback_data=f"to_btc")
            markup_curacy.add(curacy1, curacy2, curacy3)
            bot.send_message(call.message.chat.id, text="""
            Ընտրեք taradram@ vorov cankanum eq 
            grel gumari qanak@""",reply_markup=markup_curacy)

        elif call.data == "to_amd" or call.data == "to_usd" or call.data == "to_btc":
            bot.send_message(call.message.chat.id, text="greq gumari qanak@ wr@ uzum eq poxancel")
            DATA_TRANSACTION['curacy'] = str(call.data).split('_')[1].upper()
            @bot.message_handler(content_types=['text'])
            def changing_real_time(message):
                while message.text.isnumeric():
                    count_exchange = int(message.text)
                    while count_exchange >= 2000 and DATA_TRANSACTION['curacy'] == "AMD" or count_exchange >= 5 and DATA_TRANSACTION['curacy'] == "USD" or count_exchange >= 0.0000001 and DATA_TRANSACTION['curacy'] == "BTC":
                        DATA_TRANSACTION['count'] = message.text
                        one_cripto = [str(DATA_TRANSACTION['cryptocoin'].lower())]
                        Exchange = ClassApis(curacy=DATA_TRANSACTION['curacy'], count=count_exchange, cryptocoin_array=one_cripto)
                        change_count = Exchange.cripto_price()
                        DATA_TRANSACTION['count_cripto'] = change_count[0][:-9]

                        if DATA_TRANSACTION['type_transaction'] == "Buy":
                            DATA_TRANSACTION['datetime'] = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
                            bot.send_message(message.chat.id, f"""
Շնորհակալություն մեզ ընտրելու համար!
Փոխանցեք գումարը այս հաշվեհամարներից մեկին և ուղարկեք կտրոնը:

Գումարը կրիպտոյով {change_count[0][:-9]}, {DATA_TRANSACTION['type_transaction']}

            099-99-99-99 IDram Wallet
            099-99-99-99 Telcell Wallet
            099-99-99-99 EasyPay Wallet

Կտրոնի բացակայության դեպքում մենք ոչնչի համար պատասխանատվություն չենք կրում:
                        """, ) # reply_markup=markop_buy_and_sell_state

                        elif DATA_TRANSACTION['type_transaction'] == "Sell":
                            bot.send_message(message.chat.id, f"""
Շնորհակալություն մեզ ընտրելու համար!
Փոխանցեք գումարը այս հաշվեհամարներից մեկին և ուղարկեք կտրոնը:
Գումարը կրիպտոյով {change_count}, {DATA_TRANSACTION['type_transaction']}

        {wallet_data[DATA_TRANSACTION['cryptocoin'].upper()]['wallet_key']}
                            {DATA_TRANSACTION['cryptocoin']} Wallet

Կտրոնի բացակայության դեպքում մենք ոչնչի համար պատասխանատվություն չենք կրում:
""", ) # reply_markup=markop_buy_and_sell_state

                        @bot.message_handler(content_types=['photo'])
                        def handle_docs_document(message):
                            print("user")
                            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                            downloaded_file = bot.download_file(file_info.file_path)
                            src = f"{PATH}/con/photo/client_check_image_id/{message.chat.id}-{message.photo[1].file_id}.png"

                            with open(src, 'wb') as new_file:
                                new_file.write(downloaded_file)

                            DATA_TRANSACTION['client_check_image_id'] = message.photo[1].file_id

                            markup_transaction_status = types.InlineKeyboardMarkup(row_width=2)
                            type_cour1 = types.InlineKeyboardButton(text='Success', callback_data="success")
                            type_cour2 = types.InlineKeyboardButton(text='Failed', callback_data='failed')
                            markup_transaction_status.add(type_cour1, type_cour2)
                            bot.send_message(my_chat_id, text=f"{DATA_TRANSACTION}")
                            bot.send_message(my_chat_id, text="""
                            ete cheg@ liovin stugvac e sexmeq success.
                            """)

                            photo = open(src, 'rb')
                            bot.send_photo(my_chat_id, photo, reply_markup=markup_transaction_status)
                        break
                    else:
                        bot.send_message(call.message.chat.id, f"⚠️Գրեք գումարի չափը {limits_country_exchange[DATA_TRANSACTION['curacy']]}-ից սկսած")
                        break
                    break
                else:
                    bot.send_message(call.message.chat.id, '⚠️Enter the amount in number')

        elif call.data == "success":
            DATA_TRANSACTION['state_transaction'] = call.data
            bot.send_message(call.message.chat.id, "write a user id")


                # photo = open(src, 'rb')
                # bot.send_photo(user_id, photo, )

  # reply_markup=markup_transaction_status

        elif call.data == "failed":
            print(call.data)

        elif call.data == "/exit":
            pass

if __name__ == '__main__':
    bot = telebot.TeleBot(TOKEN)
    start_bot(bot)
    bot.polling(none_stop=True, interval=0)

