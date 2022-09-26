import time
import telebot
from datetime import datetime, timedelta
from run_test_loki.con.classes.conf.configuration import *
from run_test_loki.con.classes.SQL.StartingPostgres import *
from run_test_loki.con.classes.Utilites.Utils import UtilsApp

bot = telebot.TeleBot(TOKEN)

limit = limit_time_send_photo

def Starting():
    while True:

        transactions = list(Sessions.query(TransactionExchange.user_id, TransactionExchange.state_transaction,
                                           TransactionExchange.datetime).limit(30))

        for row in transactions:
            if row[2] is not None:

                date = datetime.now()

                date_stop = row[2] + timedelta(minutes=limit)

                stop_state = ("waiting_user_wallet", 'waiting_user_photo', 'waiting_user_send_id')
                print("paning")

                if date_stop.strftime('%Y.%m.%d %H:%M') < date.strftime('%Y.%m.%d %H:%M') and row[1] in stop_state:
                    DeleteInfo = UtilsApp(bot=None, message=None)
                    DeleteInfo.DelleteTransactionData(row[0])
                    bot.send_message(row[0], text=f"""
{Translate().ShowText(row[0], 46)}

{Translate().ShowText(row[0], 47)}
""")
                    print("send message to user and delete the transaction")
                time.sleep(1)
            else:
                continue

if __name__ == "__main__":
    Starting()
