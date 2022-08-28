import requests
from con.classes.conf.configuration import *
from con.classes.SQL.tables.Transactions import TransactionExchange
from con.classes.SQL.tables.conf.config import *

Transaction = TransactionExchange()
Sessions = Session()

class ClassApis():
    def __init__(self, cryptocoin_array):
        self.API = "https://min-api.cryptocompare.com/data/price"
        self.cryptocoin_array = cryptocoin_array
        self.amd_price = arm_price
        # self.Sessions = Session()
    def all_crypto_price(self):
        crypto_to_usd = []
        for cry in self.cryptocoin_array:
            params = {
                "fsym": cry.upper(),
                "tsyms": "USD",
                "api_key": "aa735b3e07ea3c717e7b6f2302221dec10089e3720e929d65a4bcc8695dca3d9",
            }
            req = requests.get(url=self.API, params=params)
            crypto_to_usd.append(req.json()["USD"])

        return crypto_to_usd

    def crypto_price_user(self, curacy, amount_user):
        for cry in self.cryptocoin_array:
            params = {
                "fsym": cry.upper(),
                "tsyms": ("AMD", curacy.upper()),
                "api_key": "aa735b3e07ea3c717e7b6f2302221dec10089e3720e929d65a4bcc8695dca3d9",
            }
            req = requests.get(url=self.API, params=params)

            result = float(amount_user) / float(req.json()[curacy.upper()])
            result_amd = float(result) * float(req.json()["AMD"])
            result_amd = str(result_amd + result_amd / 100 * float(commission)).split(".")[0][:-2] + '00'
            result_crypto = result + result / 100 * commission
            return str(result)[:11], str(result_amd)[:11], result_crypto

cryptocoin_array = ['DASH']
test = ClassApis(cryptocoin_array)
# # # test.all_crypto_price()
print(test.crypto_price_user("DASH", 1))