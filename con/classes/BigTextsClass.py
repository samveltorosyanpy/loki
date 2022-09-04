from telebot import types
from datetime import datetime
from con.classes.conf.configuration import *


class BuySellClass():
    def __init__(self, user_id, type_transaction, bot):
        self.user_id = user_id
        self.type_transaction = type_transaction
        self.bot = bot

    def InformationSendMany(self, message):
        cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        armenian_wallet = Sessions.query(TransactionExchange.armenian_wallet).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        amount_crypto_pr = Sessions.query(TransactionExchange.amount_crypto_pr).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        amd_amount_pr = Sessions.query(TransactionExchange.amd_amount_pr).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        owner_wallet = Sessions.query(TransactionExchange.owner_wallet).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]

        if self.type_transaction == 'Buy':
            self.bot.send_message(self.user_id,
                                  text=f"""
{Translate().ShowText(self.user_id, 12)}

{Translate().ShowText(self.user_id, 15)} {armenian_wallet} {wallets[str(armenian_wallet).lower()]}
{Translate().ShowText(self.user_id, 14)} {amd_amount_pr} AMD
""")

            markup_manually = types.InlineKeyboardMarkup(row_width=1)
            manual = types.InlineKeyboardButton(text=Translate().ShowText(self.user_id, 26),
                                                callback_data="manually")

            markup_manually.add(manual)
            self.bot.send_message(self.user_id, text=Translate().ShowText(self.user_id, 32),
                                  reply_markup=markup_manually)

        elif self.type_transaction == 'Sell':

            self.bot.send_message(self.user_id,
                                  text=f"""
    {Translate().ShowText(self.user_id, 12)}
    
    {Translate().ShowText(self.user_id, 15)} {cryptocoin} {owner_wallet}
    {Translate().ShowText(self.user_id, 14)} {str(amount_crypto_pr)[:11]} {cryptocoin}
    
    {Translate().ShowText(self.user_id, 13)}
            """)

    def Cack(self):

        transaction_id = Transaction.TransactionLastId(self.user_id)
        service_check_index = Sessions.query(TransactionPhoto.service_check_index).filter(
            TransactionPhoto.transaction_id == transaction_id)[0][0]
        type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        amount_user = Sessions.query(TransactionExchange.amount_user).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        user_wallet = Sessions.query(TransactionExchange.user_wallet).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        amount_crypto = Sessions.query(TransactionExchange.amount_crypto).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        curacy = Sessions.query(TransactionExchange.curacy).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        armenian_wallet = Sessions.query(TransactionExchange.armenian_wallet).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]

        if self.type_transaction == 'Buy':
            test = f"""
    Transaction № {transaction_id} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    Amount:  {str(amount_user + amount_user / 100 * float(commission))[:11]} {curacy}
    Transaction type:  {type_transaction}
    Amount in crypto:  {amount_crypto} {cryptocoin}
    {cryptocoin} account:
    {user_wallet}
    Transaction URL:
    {service_check_index}
    """
            return test
        elif self.type_transaction == 'Sell':
            test = f"""
                Transaction № {transaction_id} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

                Amount:  {str(amount_user + amount_user / 100 * float(commission))[:11]} {curacy}
                Transaction type:  {type_transaction}
                Amount in crypto:  {amount_crypto} {cryptocoin}
                {armenian_wallet} account:
                {user_wallet}
                Transaction ID:
                {service_check_index}
                """
            return test

# print(BaySellClass(1259401295, "Bay").Retryinfo())