import time
import random
from con.classes.BigTextsClass import *
from con.classes.SQL.StartingPostgres import *
from con.classes.buttons.button import ButtonsClass

class UtilsApp():
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    def RandomAdmins(self):
        admins = list(Sessions.query(TelegramUser.id).filter(
            or_(TelegramUser.user_state == "admin", TelegramUser.user_state == "owner_admin")))

        return random.choice(admins)[0]

    def DelleteTransactionData(self, user_id):

        try:

            state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(user_id))[0][0]

        except IndexError as ex:
            state_transaction = None

        if state_transaction != "success":
            try:
                Sessions.query(TransactionData).filter(
                    TransactionData.transaction_id == TransactionExchange().TransactionLastId(user_id)).delete()

                Sessions.query(TransactionExchange).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(user_id)).delete()

                Sessions.commit()
                Sessions.close()

            except Exception as ex:
                pass


        else:

            self.bot.send_message(self.message.chat.id, text=
            Translate().ShowText(self.message.chat.id, 5))

    def ChackState(self, state_transaction):

        if state_transaction is None:
            pass

        elif state_transaction == "start_transaction":
            pass

        elif state_transaction == "waiting_user_carncy":
            pass

        elif state_transaction == "waiting_user_amount":
            pass

        elif state_transaction == "waiting_user_wallet":

            self.bot.send_message(self.message.chat.id, text=Translate().ShowText(self.message.chat.id, 19),
                                  reply_markup=ButtonsClass().MarkupChoosWallet())

        elif state_transaction == "waiting_user_photo":
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(self.message.chat.id))[0][0]
            self.bot.send_message(self.message.chat.id, text=Translate().ShowText(self.message.chat.id, 42))
            BuySellClass(self.message.chat.id, type_transaction, self.bot).InformationSendMany(self.message)

        elif state_transaction == "waiting_confirm_admin":
            self.bot.send_message(self.message.chat.id,
                                  text=Translate().ShowText(self.message.chat.id, 43))

        elif state_transaction == "waiting_user_wallet_number":
            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(self.message.chat.id))[0][0]
            self.bot.send_message(self.message.chat.id,
                                  text=F"{Translate().ShowText(self.message.chat.id, 17)} {cryptocoin} {Translate().ShowText(self.message.chat.id, 18)}")

        elif state_transaction == "waiting_service_check_number":

            self.bot.send_message(self.message.chat.id,
                                  text=Translate().ShowText(self.message.chat.id, 44))

        elif state_transaction == "waiting_manual_time":

            self.bot.send_message(self.message.chat.id,
                                  text=f"{Translate().ShowText(self.message.chat.id, 28)} '20:00-20:30'")

        elif state_transaction == "waiting_manual_amount":

            self.bot.send_message(self.message.chat.id,
                                  text=Translate().ShowText(self.message.chat.id, 29))


        elif state_transaction == "waiting_service_check_number":

            self.bot.send_message(self.message.chat.id,
                                  text=Translate().ShowText(self.message.chat.id, 44))

        elif state_transaction == "waiting_user_send_id":
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(self.message.chat.id))[0][0]
            self.bot.send_message(self.message.chat.id, text=Translate().ShowText(self.message.chat.id, 42))
            BuySellClass(self.message.chat.id, type_transaction, self.bot).InformationSendMany(self.message)

        elif state_transaction == "success":
            pass
