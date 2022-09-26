import time
from telebot import types
from datetime import datetime
from con.classes.Binance import BnanceApi
from con.classes.conf.configuration import *
from con.classes.buttons.button import ButtonsClass



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
            owner_wallet = wallets[str(armenian_wallet).lower()]

            Transaction.ValueUpdate(
                value={"owner_wallet": owner_wallet}, id=message.chat.id)

            self.bot.send_message(self.user_id,
                                  text=f"""
{Translate().ShowText(self.user_id, 12)}

{Translate().ShowText(self.user_id, 16)} AMD: `{amd_amount_pr}`  ↘️
{Translate().ShowText(self.user_id, 15)} {armenian_wallet} `{owner_wallet}`

{Translate().ShowText(self.user_id, 48)}
""", parse_mode='MarkdownV2')
            time.sleep(5)

            self.bot.send_message(self.user_id, text=Translate().ShowText(self.user_id, 32),
                                  reply_markup=ButtonsClass().MarkupManually(self.user_id))

        elif self.type_transaction == 'Sell':

            self.bot.send_message(self.user_id,
                                  text=f"""
{Translate().ShowText(self.user_id, 45)}

{Translate().ShowText(self.user_id, 16)}  AMD: `{str(amd_amount_pr)}`
{Translate().ShowText(self.user_id, 16)}  {str(cryptocoin).upper()}: `{str(amount_crypto_pr)}`

{Translate().ShowText(self.user_id, 15)}             ⬇            `{str(cryptocoin).upper()}`
`{owner_wallet}`

{Translate().ShowText(self.user_id, 48)}
            """, parse_mode="MarkdownV2")

    def Cack(self):

        transaction_id = Transaction.TransactionLastId(self.user_id)
        service_check_index = Sessions.query(TransactionData.service_check_index).filter(
            TransactionData.transaction_id == transaction_id)[0][0]
        type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        amount_crypto_pr = Sessions.query(TransactionExchange.amount_crypto_pr).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        user_wallet = Sessions.query(TransactionExchange.user_wallet).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        armenian_wallet = Sessions.query(TransactionExchange.armenian_wallet).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]
        amd_amount_pr = Sessions.query(TransactionExchange.amd_amount_pr).filter(
            TransactionExchange.transaction_id == transaction_id)[0][0]


        if self.type_transaction == 'Buy':
            test = f"""
Transaction № {transaction_id} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Amount:  {amd_amount_pr} AMD
Transaction type:  {type_transaction}
Amount in crypto:  {amount_crypto_pr} {cryptocoin}
{cryptocoin} account:
{user_wallet}
Transaction ID:
{service_check_index}
"""
            return test
        elif self.type_transaction == 'Sell':
            test = f"""
Transaction № {transaction_id} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Amount:  {amount_crypto_pr} {cryptocoin}
Transaction type:  {type_transaction}
Amount in crypto:  {amount_crypto_pr} {cryptocoin}
{armenian_wallet} account: {user_wallet}
Transaction ID: {service_check_index}
"""
            return test