from con.classes.conf.configuration import *
from con.classes.SQL.StartingPostgres import *


class ButtonsClass():
    def __init__(self):
        pass

    def MarkupStart(self, message):

        markup = types.InlineKeyboardMarkup(row_width=2)

        type_cour1 = types.InlineKeyboardButton(text='❌  BTC', callback_data="btc")
        type_cour2 = types.InlineKeyboardButton(text='✅ DASH', callback_data='dash')
        type_cour3 = types.InlineKeyboardButton(text='❌ USDT', callback_data='usdt')
        type_cour4 = types.InlineKeyboardButton(text='❌  XRP', callback_data='xrp')
        type_cour5 = types.InlineKeyboardButton(text=Translate().ShowText(message.chat.id, 2),
                                                callback_data='ShowPrice')

        return markup.add(type_cour1, type_cour2, type_cour3, type_cour4, type_cour5)

    def MarkupLanguage(self):

        markup = types.InlineKeyboardMarkup(row_width=1)

        type_language1 = types.InlineKeyboardButton(text='🇦🇲 Հայերեն', callback_data="armenian_language")
        type_language2 = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian_language')
        type_language3 = types.InlineKeyboardButton(text='🇬🇧 English', callback_data='english_language')

        return markup.add(type_language1, type_language2, type_language3)

    def MarkupBuySell(self, message, data):
        markup = types.InlineKeyboardMarkup(row_width=2)

        type_buy = types.InlineKeyboardButton(text=Translate().ShowText(message.chat.id, 6),
                                              callback_data=f"Buy|{data}")
        type_sell = types.InlineKeyboardButton(text=Translate().ShowText(message.chat.id, 7),
                                               callback_data=f"Sell|{data}")

        return markup.add(type_buy, type_sell)

    def MarkupReadAmount(self, cryptocoin):

        markup = types.InlineKeyboardMarkup(row_width=3)

        curacy1 = types.InlineKeyboardButton(text=f"AMD", callback_data=f"to_amd")
        curacy2 = types.InlineKeyboardButton(text=f"USD", callback_data=f"to_usd")
        curacy3 = types.InlineKeyboardButton(text=f"{cryptocoin.upper()}",
                                             callback_data=f"to_{cryptocoin.lower()}")

        return markup.add(curacy1, curacy2, curacy3)

    def MarkupChoosWallet(self):

        markup = types.InlineKeyboardMarkup(row_width=2)

        type_wallet1 = types.InlineKeyboardButton(text='Idram', callback_data="Idram")
        type_wallet2 = types.InlineKeyboardButton(text='Telcell', callback_data='Telcell')
        type_wallet3 = types.InlineKeyboardButton(text='Easypay', callback_data='Easypay')

        return markup.add(type_wallet1, type_wallet2, type_wallet3)

    def MarkupConfirm(self,message):

        markup = types.InlineKeyboardMarkup(row_width=2)

        type_cour1 = types.InlineKeyboardButton(text='confirm',
                                                callback_data=f"confirm|{message.chat.id}")
        type_cour2 = types.InlineKeyboardButton(text='Cancel',
                                                callback_data=f'CancelCheck_{message.chat.id}')

        return markup.add(type_cour1, type_cour2)

    def MarkupSend(self, message):
        markup = types.InlineKeyboardMarkup(row_width=2)

        type_cour1 = types.InlineKeyboardButton(text='send',
                                                callback_data=f"send_crypto|{message.chat.id}")
        type_cour2 = types.InlineKeyboardButton(text='Cancel',
                                                callback_data=f'cancel_crypto|{message.chat.id}')

        return markup.add(type_cour1, type_cour2)

    def MarkupManually(self, user_id):

        markup_manually = types.InlineKeyboardMarkup(row_width=1)

        manual = types.InlineKeyboardButton(text=Translate().ShowText(user_id, 26),
                                            callback_data="manually")

        return markup_manually.add(manual)

    def MarkupRead(self, pr_text):

        markup_pr = types.InlineKeyboardMarkup(row_width=1)

        markup1 = types.InlineKeyboardButton(text=pr_text, callback_data="read_rp")

        return markup_pr.add(markup1)
