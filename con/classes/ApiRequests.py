import requests as req1
from con.classes.conf.configuration import *
from con.classes.SQL.StartingPostgres import *

arm_price = 400
commission = 5


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

    def crypto_price_user(self, id_u):
        user_id = id_u
        amount_user = Sessions.query(TransactionExchange.amount_user).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                user_id))[0][0]
        cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                user_id))[0][0]
        curacy = Sessions.query(TransactionExchange.curacy).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                user_id))[0][0]

        params = {
            "fsym": cryptocoin,
            "tsyms": ("USD", curacy),
            "api_key": "aa735b3e07ea3c717e7b6f2302221dec10089e3720e929d65a4bcc8695dca3d9",
        }

        req = req1.get(url=self.API, params=params)

        price_crypto = req.json().get("USD")
        price_to_amd = price_crypto * arm_price
        # price_to_amd_pr = price_to_amd + price_to_amd * commission / 100

        if curacy == "AMD":
            price_crypto = price_crypto * arm_price

        else:
            price_crypto = req.json().get(curacy)

        PRICE_CRYPTO_PR = amount_user / (price_crypto + price_crypto * commission / 100)
        print(PRICE_CRYPTO_PR)

            # # amoun_to_crypto = float(amount_user) / float(price_crypto[curacy.upper()])
            # amount_to_amd = price_crypto['USD'] * arm_price

            # amount_to_amd_pr = None
            # amount_to_crypto_pr = None

            # if pr_read == True:
            #     # tokos@ hashvum enq cryptoi mech
            #10000
            #     if type_transaction == "Sell":
            #         # print()
            #         amount_to_crypto_pr = amount_to_crypto + amount_to_crypto * 5 / 100
            #         # print("Sell, kamisyan mtnum e cryptoi mech")
            #
            #     elif type_transaction == "Buy":
            #         # pass
            #         amount_to_crypto_pr = amount_to_crypto - amount_to_crypto * 5 / 100
            #         # print("Buy, kamisyan mtnuma cryptoi mech")
            #
            # elif pr_read == False:
            #     # tokos@ hashvum enq drami mech
            #
            #     if type_transaction == "Sell":
            #         # pass
            #         amount_to_amd_pr = str(amount_to_amd - amount_to_amd * 5 / 100).split(".")[0][:-2] + '00'
            #         # print("Sell, kamisyan mtnuma drami mech")
            #
            #     elif type_transaction == "Buy":
            #         # pass
            #         amount_to_amd_pr = str(amount_to_amd + amount_to_amd * 5 / 100).split(".")[0][:-2] + '00'
            #         # print("Buy, kamisyan mtnuma drami mech")
            #
            # return str(amount_to_amd_pr).split(".")[0][:-2] + '00', str(amount_to_crypto_pr)[:11], str(
            #     amount_to_crypto)[:11]

cryptocoin_array = ['DASH']
test = ClassApis(cryptocoin_array)
# test.all_crypto_price()amount_crypto
p = test.crypto_price_user(1259401295)


# 0.56472984 Dash
# 0.57024316 Dash
