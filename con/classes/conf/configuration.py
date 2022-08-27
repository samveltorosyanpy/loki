from con.classes.SQL.StartingPostgres import *
import os

TOKEN = os.environ['TOKEN']
# TOKEN = "5309521467:AAEDLFgC-3J6GpcD4ImA2ZyEMvtKLCYcoRs"
APP_URL = f"https://lokichangebot.herokuapp.com/{TOKEN}"

limit_time_send_photo = Sessions.query(ChangeInformation.limit_time_send_photo).filter(
    ChangeInformation.id == 1)[0][0]  # minutes


PATH = os.path.dirname(__file__)[:-17]


commission = Sessions.query(ChangeInformation.commission).filter(
    ChangeInformation.id == 1)[0]  # %


owner_id = Sessions.query(ChangeInformation.owner_id).filter(ChangeInformation.id == 1)[0][0]


arm_price = Sessions.query(ChangeInformation.amd_price).filter(ChangeInformation.id == 1)[0][0]

min_limits_amount_exchange = {
    "AMD": Sessions.query(ChangeInformation.min_limits_amount_exchange_amd).filter(ChangeInformation.id == 1)[0][0],
    "USD": Sessions.query(ChangeInformation.min_limits_amount_exchange_usd).filter(ChangeInformation.id == 1)[0][0],
    "BTC": Sessions.query(ChangeInformation.min_limits_amount_exchange_btc).filter(ChangeInformation.id == 1)[0][0],
    "DASH": Sessions.query(ChangeInformation.min_limits_amount_exchange_dash).filter(ChangeInformation.id == 1)[0][0],
    "XRP": Sessions.query(ChangeInformation.min_limits_amount_exchange_xrp).filter(ChangeInformation.id == 1)[0][0],
    "LTC": Sessions.query(ChangeInformation.max_limits_amount_exchange_ltc).filter(ChangeInformation.id == 1)[0][0],
}

max_limits_amount_exchange = {
    "AMD": Sessions.query(ChangeInformation.max_limits_amount_exchange_amd).filter(ChangeInformation.id == 1)[0][0],
    "USD": Sessions.query(ChangeInformation.max_limits_amount_exchange_usd).filter(ChangeInformation.id == 1)[0][0],
    "BTC": Sessions.query(ChangeInformation.max_limits_amount_exchange_btc).filter(ChangeInformation.id == 1)[0][0],
    "DASH": Sessions.query(ChangeInformation.max_limits_amount_exchange_dash).filter(ChangeInformation.id == 1)[0][0],
    "XRP": Sessions.query(ChangeInformation.max_limits_amount_exchange_xrp).filter(ChangeInformation.id == 1)[0][0],
    "LTC": Sessions.query(ChangeInformation.max_limits_amount_exchange_ltc).filter(ChangeInformation.id == 1)[0][0],
}

wallet_data = {
    'BTC': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_btc).filter(ChangeInformation.id == 1)[0][0],
    },
    'DASH': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_dash).filter(ChangeInformation.id == 1)[0][0],
    },
    'LTC': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_ltc).filter(ChangeInformation.id == 1)[0][0],
    },
    'XRP': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_xrp).filter(ChangeInformation.id == 1)[0][0],
    },
    'Idram': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_idram).filter(ChangeInformation.id == 1)[0][0],
    },
    'Telcell': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_telcell).filter(ChangeInformation.id == 1)[0][0],
    },
    'Easypay': {
        'wallet_key': Sessions.query(ChangeInformation.owner_walet_easypay).filter(ChangeInformation.id == 1)[0][0],
    },
}

SENTENCE_BOT = {
    "armenian": [
        "Ընտրել կրիպտոարժույթը 🏦",  # 0
        "📊 Տեսնել կրիպտոների արժույթը",  # 1
        "🏴‍☠️Ընտրեք բոտի լեզուն",  # 2
        "Ընտրեք արտարժույթը",  # 3
        "Սեղմեք /start, որպեսզի սկսեք կրկին",  # 4
        "Գնել",  # 5
        "Վաճառել",  # 6
        "💱 Ընտրեք գործարքի տեսակը",  # 7
        ["Կրիպտոարժույթների գինը  այս պահի դրությամբ:",
         "Ուշադրություն, գինը կարող է փոքր ինչ տարբերություն տալ շուկայականից"],
        # 8.1, 8.2
        "Գրեք գումարի ցանկալի քանակը փոխանցման համար",  # 9
        ["Փոխանցեք գումարը հաշիվներն և ուղարկեք կտրոն",
         "Կտրոնի բացակայության դեպքում մենք հետևանքների համար պատասխանատվություն չենք կրում", "Գումարը Կրիպտոարժույթով",
         "Մեր հաշվեհամարը", "Գումարի քանակը"],
        # 10.1, 10.2, 10.3, 10.4
        ["Խնդրում ենք գրել ձեր ", "հաշվեհամարը"],  # 11.1, 11.2
        "Ընտրեք ցանկալի դրամապանակը",  # 12
        "⚠  գրեք գումարի քանակը ոչ պակաս",  # 13
        "⚠  Մուտքագրեք գումարը թվանշաններով",  # 14
        "Ձեր փոխանցումը հաջողությամբ կատարված է",  # 15
        "Ձեր կտրոնը մերժվել է, խնդրում ենք ուղարկել կրկին կամ կապ հաստատել օպերատրի հետ @cuturie",  # 16
        "Լեզուն փոխվել է, սեղմեք /start",  # 17
        "💥 գործարքը կանգնեցված է նշված ընթացքում կտրոնը չուղարկելու պատճառով:",  # 18
        "Լրացնել ձեռքով"  # 19

        "Ուղարկեք ավելի հստակ նկար",
        "Գրեք գործարքի մոտավոր ժամանակը հետևյալ ձևով '20:00-20:30'",
        "Գրեք ուղարկված գումարի չափը",
        "Կխնդրենք հետևել տվյած ձևին '20:00-20:30'",
        "Օգտատերը չունի չեկ, կխնդրեմ ստուգել դրա առկայությունը տրված ժամով և գումարի քանակով",
        "Եթե չունեք չեկ, սեղմեք Լրացնել ձեռքով կոճակը",
        "Եթե չեկը լիովին ստուգված է, սեղմեք Confirm և ուղարկեք բլոկչեյնի հղումը",
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
        ["Переведите сумму на один из этих счетов и отправьте купон",
         "При отсутствии купона мы не несем ответственности за последствия", "Сумма в криптовалюте", "Наш счет",
         "Количество денег"],
        ["Пожалуйста, напишите свой номер", "счета"],
        "Выберите нужный кошелек",
        "⚠️ запишите количество денег не меньше",
        "⚠  введите сумму цифрами",
        "Ваш перевод прошел успешно",
        "Ваш купон отклонен, пожалуйста, отправьте его еще раз или свяжитесь с оператором @cuturie.",
        "Язык изменен, нажмите /start",
        "💥 сделка отменена по причине истечении времени ожидания отправки купона",
        "Введите вручную",

        "Отпраьте более четкую фотографию",
        "Запишите примерное время совершения транзакции в данном формате '20:00-20:30'",
        "Запишите переведенную сумму",
        "Придерживайтесь указанного формата '20:00-20:30'",
        "У пользователя нету чека, прошу проверить наличие чека с указанным временем и суммой",
        "Если у вас нету чека, то нажмите на кнопку 'Введите вручную'",
        "Если чек полностью проверен, нажмите 'Confirm' и отправьте ссылку блокчейна",
    ],

    "english": [
        "Select cryptocurrency 🏦", #+
        "📊 cryptocurrency prices", #+
        "🏴‍☠ choose a language for the bot",
        "Choose your currency",
        "Press /start to start again",
        "Buy",
        "Sell",
        "💱 Select the transaction type",
        ["The price of cryptocurrencies at the moment",
         "Attention, the price may give a small difference from market's"],
        "Write down the amount of money you want to transfer",
        ["Transfer the money to one of these accounts and send the coupon",
         "In case of absence of a coupon, we are not responsible for the consequences.", "Amount in cryptocurrency",
         "Our account", "Amount of money"],
        ["Please write your account", "wallet"],
        "Choose the wallet that suits you",
        "⚠  write down the amount of money at least",
        "⚠  enter the amount with numbers",
        "Your transfer was successful",
        "Your coupon is rejected, please send again or contact the operator @cuturie",
        "The language has been changed, press /start",
        "💥 the transaction is suspended due to ending of the specified time of sending the invoice",
        "Enter manually",

        "Send more accurate image",
        "Write the approximate time of transaction in this form '20:00-20:30'",
        "Write the sent amount",
        "Please, follow the form '20:00-20:30'",
        "User doesn't have the invoice, please check the presence of it by this date and amount",
        "If you don't have the invoice, press the 'Enter manually' button",
        "If the invoice is fully checked, press 'Confirm' and send blockchain link",
    ]
}
