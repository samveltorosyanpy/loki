import requests

class ClassApis():
    def __init__(self, curacy, count, cryptocoin_array):
        self.API = "https://yobit.net/api/3/ticker"
        self.API_CURACY = "https://api.exchangerate.host/latest"
        self.cryptocoin_array = cryptocoin_array
        self.curacy = curacy
        self.count = count

    def cripto_price(self):
        curacy = "USD" if self.curacy is None else self.curacy
        cryptos = self.cryptocoin_array
        cripto_to_usd = []
        params_curacy = {
            'base': "USD",
            'symbols': curacy,
        }
        req_curacy = requests.get(url=self.API_CURACY, params=params_curacy)
        price_curacy = float(req_curacy.json()['rates'][curacy])

        for cry in cryptos:

            API = f"{self.API}/{cry}_usd"
            req = requests.get(url=API)
            req_price_crypto = str(req.json()[cry+"_usd"].get('sell')).split('.')
            if self.count is None:

                price_curacy_res = req_price_crypto[0] + "." + req_price_crypto[1][:6]
                result = float(price_curacy_res) * price_curacy

            else:

                price_curacy_res = req_price_crypto[0] + "." + req_price_crypto[1][:6]
                result = float(self.count) / (float(price_curacy_res ) * price_curacy)

            cripto_to_usd.append(f"{str(result)}")

        return cripto_to_usd



# sum = 1000
# to = 'bay'
# cryptocoin_array = ['btc']
#
# test = ClassApis(curacy="AMD", count=10000, cryptocoin_array=cryptocoin_array)
# test.cripto_price()
