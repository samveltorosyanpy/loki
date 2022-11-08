import requests as req1
from con.classes.conf.configuration import *
from con.classes.SQL.StartingPostgres import *

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
            req = req1.get(url=self.API, params=params)
            crypto_to_usd.append(req.json()["USD"])

        return crypto_to_usd

    def crypto_price_user(self, message):
        user_id = message.chat.id
        # user_id = message
        amount_user = Sessions.query(TransactionExchange.amount_user).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                user_id))[0][0]
        cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                user_id))[0][0]
        curacy = Sessions.query(TransactionExchange.curacy).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                user_id))[0][0]
        print("amount_user: ", amount_user, "\n")

        params = {
            "fsym": cryptocoin,
            "tsyms": ("USD", curacy),
            "api_key": "aa735b3e07ea3c717e7b6f2302221dec10089e3720e929d65a4bcc8695dca3d9",
        }

        req = req1.get(url=self.API, params=params)

        price_crypto = req.json().get("USD")
        price_to_amd = price_crypto * arm_price
        print("price_crypto: ", price_crypto, " price_to_amd: ", price_to_amd, "\n")

        if curacy == "AMD":
            crypto_price = amount_user / price_to_amd
            amd_price_pr = amount_user + amount_user * 5 / 100
            crypto_price_pr = crypto_price + crypto_price * commission / 100
            return amd_price_pr, crypto_price_pr, crypto_price

        elif curacy == "USD":
            amd_price = amount_user * arm_price
            amd_price_pr = amd_price + amd_price * 5 / 100
            crypto_price = amount_user / price_crypto
            crypto_price_pr = crypto_price + crypto_price * commission / 100
            return amd_price_pr, crypto_price_pr, crypto_price

        else:
            amd_price = amount_user * price_to_amd
            amd_price_pr = amd_price + amd_price * 5 / 100
            crypto_price_pr = amount_user + amount_user * commission / 100
            return amd_price_pr, crypto_price_pr, amount_user

# cryptocoin_array = ['DASH']
# test = ClassApis(cryptocoin_array)
# # test.all_crypto_price()
# d = test.crypto_price_user(1259401295)
# print(d)
