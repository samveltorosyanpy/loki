import requests

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
            req = requests.get(url=self.API, params=params)
            crypto_to_usd.append(req.json()["USD"])

        return crypto_to_usd

    def crypto_price_user(self, curacy, amount_user, pr_read, type):

        for cry in self.cryptocoin_array:

            params = {
                "fsym": cry.upper(),
                "tsyms": ("AMD", curacy.upper()),
                "api_key": "aa735b3e07ea3c717e7b6f2302221dec10089e3720e929d65a4bcc8695dca3d9",
            }

            req = requests.get(url=self.API, params=params)

            price = req.json()
            print(price)

            amoun_to_crypto = float(amount_user) / float(price[curacy.upper()])
            amoun_to_amd = float(price["AMD"]) * amoun_to_crypto
            amoun_to_crypto_pr = float(amount_user) / float(price[curacy.upper()])
            amoun_to_amd_pr = float(price["AMD"]) * amoun_to_crypto

            if pr_read == True:
                # tokos@ hashvum enq cryptoi mech

                if type == "Sell":

                    amoun_to_crypto_pr = amoun_to_crypto + amoun_to_crypto * 5 / 100
                    print("Sell, kamisyan mtnum e cryptoi mech")

                elif type == "Buy":

                    amoun_to_crypto_pr = amoun_to_crypto - amoun_to_crypto * 5 / 100
                    print("Buy, kamisyan mtnuma cryptoi mech")

            elif pr_read == False:
                # tokos@ hashvum enq drami mech

                if type == "Sell":
                    amoun_to_amd_pr = str(amoun_to_amd - amoun_to_amd * 5 / 100).split(".")[0][:-2] + '00'
                    print("Sell, kamisyan mtnuma drami mech")

                elif type == "Buy":
                    amoun_to_amd_pr = amoun_to_amd + amoun_to_amd * 5 / 100
                    print("Buy, kamisyan mtnuma drami mech")

            return str(amoun_to_amd_pr).split(".")[0][:-2] + '00', str(amoun_to_crypto_pr)[:11], str(amoun_to_crypto)[:11]

# cryptocoin_array = ['DASH']
# test = ClassApis(cryptocoin_array)
# # test.all_crypto_price()amount_crypto
# print(test.crypto_price_user(curacy="AMD", amount_user=10000, pr_read=True, type="Sell"))




# 0.56472984 Dash
# 0.57024316 Dash