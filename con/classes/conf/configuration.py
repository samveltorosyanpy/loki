import os


PATH = os.path.dirname(__file__)[:-17]
TOKEN = '5728675320:AAEnXeGckEN2yGpyI_XzDPhpVo-pLeqy9KQ'

APP_URL = f"https://mybotchanger.herokuapp.com/{TOKEN}"

limit_time_send_photo = 20 # minutes

commission = 5 # %

limits_amount_exchange = {
    "AMD": 2000,
    "USD": 10,
    "BTC": 1,
    "DASH": 1,
    "XRP": 1,
    "LTC": 1,
}
arm_price = 400


SENTENCE_BOT = {
    "armenian": [
                    "Ընտրել կրիպտոարժույթը 🏦",   #0
                    "📊 Տեսնել կրիպտոների արժույթը",  #1
                    "🏴‍☠️Ընտրեք բոտի լեզուն",  #2
                    "Ընտրեք արտարժույթը", #3
                    "Սեղմեք /start, որպեսզի սկսեք կրկին", #4
                    "Գնել", #5
                    "Վաճառել", #6
                    "💱 Ընտրեք գործարքի տեսակը", #7
                    ["Կրիպտոարժույթների գինը  այս պահի դրությամբ:", "Ուշադրություն, գինը կարող է փոքր ինչ տարբերություն տալ շուկայականից"], #8.1, 8.2
                    "Գրեք գումարի ցանկալի քանակը փոխանցման համար", #9
                    ["Փոխանցեք գումարը այդ հաշիվներից մեկին և ուղարկեք կտրոն", "Կտրոնի բացակայության դեպքում մենք հետևանքների համար պատասխանատվություն չենք կրում", "Գումարը Կրիպտոարժույթով", "Մեր հաշվեհամարը", "Գումարի քանակը"], #10.1, 10.2, 10.3, 10.4
                    ["Խնդրում ենք գրել ձեր ", "հաշվեհամարը"], # 11.1, 11.2
                    "Ընտրեք ցանկալի դրամապանակը", #12
                    "⚠  գրեք գումարի քանակը ոչ պակաս", # 13
                    "⚠  Մուտքագրեք գումարը թվանշաններով", # 14
                    "Ձեր փոխանցումը հաջողությամբ կատարված է", # 15
                    "Ձեր կտրոնը մերժվել է, խնդրում ենք ուղարկել կրկին կամ կապ հաստատել օպերատրի հետ @cuturie", # 16
                    "Լեզուն փոխվել է, սեղմեք /start", # 17
                    "💥 գործարքը կանգնեցված է նշված ընթացքում կտրոնը չուղարկելու պատճառով:", # 18
                    "Լրացնել ձեռքով" # 19
                    ],








    "russian": [
                    "Выберите криптовалюту 🏦",
                    "📊 цены на криптовалюты",
                    "🏴‍☠ выберите язык для бота",
                    "Укажите валюту",
                    "Нажмите /start, чтобы начать снова",
                    "Купить",
                    "Продать",
                    "💱 Выберите тип транзакции",
                    ["Цены криптовалют на данный момент", "Внимание, цена может дать небольшую разницу от рыночной"],
                    "Запишите сумму, которую вы хотите перевести",
                    ["Переведите сумму на один из этих счетов и отправьте купон", "При отсутствии купона мы не несем ответственности за последствия", "Сумма в криптовалюте", "Наш счет", "Количество денег"],
                    ["Пожалуйста, напишите свой номер", "счета"],
                    "Выберите нужный кошелек",
                    "⚠️ запишите количество денег не меньше",
                    "⚠  введите сумму цифрами",
                    "Ваш перевод прошел успешно",
                    "Ваш купон отклонен, пожалуйста, отправьте его еще раз или свяжитесь с оператором @cuturie.",
                    "Язык изменен, нажмите /start",
                    "💥 сделка отменена по причине истечении времени ожидания отправки купона",
                    "Введите вручную"
                    ],








    "english": [
                    "Select cryptocurrency 🏦",
                    "📊 cryptocurrency prices",
                    "🏴‍☠ choose a language for the bot",
                    "Choose your currency",
                    "Press /start to start again",
                    "Buy",
                    "Sell",
                    "💱 Select the transaction type",
                    ["The price of cryptocurrencies at the moment", "Attention, the price may give a small difference from market's"],
                    "Write down the amount of money you want to transfer",
                    ["Transfer the money to one of these accounts and send the coupon", "In case of absence of a coupon, we are not responsible for the consequences.", "Amount in cryptocurrency", "Our account", "Amount of money"],
                    ["Please write your account", "wallet"],
                    "Choose the wallet that suits you",
                    "⚠  write down the amount of money at least",
                    "⚠  enter the amount with numbers",
                    "Your transfer was successful",
                    "Your coupon is rejected, please send again or contact the operator @cuturie",
                    "The language has been changed, press /start",
                    "💥 the transaction is suspended due to ending of the specified time of sending the invoice",
                    "Enter manually"
                    ]
}



wallet_data = {
    'BTC': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'DASH': {
        'wallet_key': 'Xf7ucLPzPECcVrA5Us1vbeByGdPw6bgErQ',
        'server': ''
        ## fantasy duck flee dismiss great upgrade lesson they match exotic strike print
    },
    'LTC': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'XRP': {
        'wallet_key': '3J6GpcD4ImA2ZyEMvtKLCYcoRs',
        'server': ''
    },
    'Idram': {
        'wallet_key': '099-99-99-99',
    },
    'Telcell': {
        'wallet_key': '099-99-99-99',
    },
    'Easypay': {
        'wallet_key': '099-99-99-99',
    },
}

# 2.15
