# from binance.spot import Spot
from binance.exceptions import BinanceAPIException
from binance.client import Client
from con.classes.conf.configuration import *
import requests

client = Client(api_key, api_secret)

# https://python-binance.readthedocs.io/en/latest/
class BnanceApi():
    def __init__(self, crypto):
        self.address = client.get_deposit_address(coin='DASH').get("address")
        self.crypto = str(crypto).upper()
        
    def SendCrypto(self, user_address, amount, description):
        # order = client.create_test_order(
        #     symbol=f'{self.crypto.upper()}USDT',
        #     side=Client.SIDE_BUY,
        #     type=Client.ORDER_TYPE_MARKET,
        #     quantity=amount)
        # print(order)
        try:
            # name parameter will be set to the asset value by the client if not passed
            # result = client.withdraw(
            #     coin=self.crypto,
            #     address=user_address,
            #     amount=amount,
            #     name=description)
            # id = result["id"]
            id = "1656116512321685454486"
            return id
        except BinanceAPIException as ex:
            print(ex)
        else:
            print("Success")

# BnanceApi("DASH").SendCrypto(BnanceApi("DASH").address, 0.545, "description")





