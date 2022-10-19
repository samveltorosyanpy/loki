from binance.exceptions import BinanceAPIException
from binance.client import Client
from con.classes.conf.configuration import *
#
client = Client(api_key, api_secret)

# https://python-binance.readthedocs.io/en/latest/
class BnanceApi():
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message
        self.address = "XjEa7wZtnSeLCawTM1c5B4tME1YD9x6PPR"
        # self.address = client.get_deposit_address(coin=self.crypto).get("address")

    def SendCrypto(self, crypto, user_address, amount, description, user_id):
        """qomentvac funkcian katarum e konvertacia usdt-i ev @ntrvac coini het anmijapes uxarkelov
        gumar@ nshvac hasceyov: qani vor ays pahin statik ip chunem na chi ashxatum"""

        trans_id = TransactionExchange().TransactionLastId(user_id)
        trx_id = Sessions.query(TransactionExchange.admin_id).filter(
                TransactionExchange.transaction_id == trans_id)[0][0]
        return(trx_id)


        # order = client.create_test_order(
        #     symbol=f'{self.crypto.upper()}USDT',
        #     side=Client.SIDE_BUY,
        #     type=Client.ORDER_TYPE_MARKET,
        #     quantity=amount)
        # print(order)
        # try:
        #     result = client.withdraw(
        #         coin=self.crypto,
        #         address=user_address,
        #         amount=amount,
        #         name=description)
        #     id = result["id"]
        #     return id
        # except BinanceAPIException as ex:
        #     print(ex)
        # else:
        #     print("Success")

