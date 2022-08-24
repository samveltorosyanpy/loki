import telebot
import schedule
from time import sleep
from datetime import datetime, timedelta
from con.classes.conf.configuration import *
from con.classes.SQL.StartingPostgres import *

bot = telebot.TeleBot(TOKEN)
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def waiting():
    # await asyncio.sleep(5)
    while True:
        transaction_list = list(Sessions.query(TransactionExchange.transaction_id, TransactionExchange.user_id, TransactionExchange.datetime, TransactionExchange.state_transaction).filter(TransactionExchange.state_transaction == 'waiting_user_photo').group_by(TransactionExchange.transaction_id).order_by(TransactionExchange.transaction_id.desc()))
        for row in transaction_list:
            try:
                datet = datetime.strptime(row[2].strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S") + timedelta(minutes=limit_time_send_photo)
                if datet <= datetime.now():
                    print("send message")

                else:
                    continue

            except AttributeError as ex:
                continue


def bot_start(bot):

    @bot.message_handler(commands=["start"])
    def choose_transaction(message):
        bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot_start(bot)
    schedule.every().saturday.at("18:28").do(waiting)
    bot.polling(none_stop=True, interval=0)
# main_loop = asyncio.get_event_loop()
# cors = asyncio.wait([waiting(), bot_start(bot)])
# main_loop.run_until_complete(cors)
# main_loop.run_forever()




# .strftime("%m/%d/%Y, %H:%M:%S")