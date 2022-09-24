# from binance.spot import Spot
from binance.exceptions import BinanceAPIException
from binance.client import Client
from con.classes.conf.configuration import *

client = Client(api_key, api_secret)

class BnanceApi():
    def __init__(self, crypto):
        self.address = client.get_deposit_address(coin='DASH').get("address")
        self.crypto = str(crypto).upper()
    def SendCrypto(self, user_address, amount, transaction_id):
        try:
            # name parameter will be set to the asset value by the client if not passed
            result = client.withdraw(
                coin=self.crypto,
                address=user_address,
                amount=amount,
                name=transaction_id)
        except BinanceAPIException as e:
            print(e)
        else:
            print("Success")


