import time
from con.classes.BigTextsClass import *

class UtilsApp():
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    def WaitingAdmin(self, chat_id):
        text = Translate().ShowText(chat_id, 39)
        sm = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]
        self.bot.send_message(chat_id, text=f"{text} {sm[0]}")

        for id in range(1, len(sm)):
            self.bot.edit_message_text(text=f"{text} {sm[id]}", chat_id=chat_id,
                                  message_id=self.message.message_id + 1)
            time.sleep(0.1)

    def ChackState(self):
        try:
            state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(self.message.chat.id))[0][0]
        except IndexError as ex:
            state_transaction = None

        if state_transaction is None:
            skip = True
            return skip

        elif state_transaction == "starting_transaction":
            skip = True
            return skip

        elif state_transaction == "waiting_user_amount":
            skip = True
            return skip

        elif state_transaction == "waiting_user_wallet":
            skip = True
            return skip

        elif state_transaction == "waiting_user_wallet":
            skip = True
            return skip

        elif state_transaction == "waiting_user_photo":
            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(self.message.chat.id))[0][0]
            self.bot.send_message(self.message.chat.id, text="duq arden uneq bacvac transactia xndrum enq sharunakel ayn kam kanchel /clear vorpesi skseq noric")
            BuySellClass(self.message.chat.id, type_transaction, self.bot).InformationSendMany(self.message)
            skip = False
            return skip

        elif state_transaction == "waiting_admin_wallet_write":
            UtilsApp(self.bot, self.message).WaitingAdmin(self.message.chat.id)
            skip = False
            return skip

        elif state_transaction == "waiting_user_wallet_number":
            cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                TransactionExchange.transaction_id == Transaction.TransactionLastId(self.message.chat.id))[0][0]
            self.bot.send_message(self.message.chat.id,
                                  text=F"{Translate().ShowText(self.message.chat.id, 17)} {cryptocoin} {Translate().ShowText(self.message.chat.id, 18)}")
            skip = False
            return skip

        elif state_transaction == "waiting_service_check_number":

            self.bot.send_message(self.message.chat.id,
                                  text=F"der poxancum@ @ntacqi mech e xndrum enq spasel")
            skip = False
            return skip



        elif state_transaction == "waiting_manual_time":

            self.bot.send_message(self.message.chat.id,
                                  text=f"{Translate().ShowText(self.message.chat.id, 28)} '20:00-20:30'")
            skip = False
            return skip

        elif state_transaction == "waiting_manual_amount":

            self.bot.send_message(self.message.chat.id,
                                  text=Translate().ShowText(self.message.chat.id, 29))
            skip = False
            return skip

        elif state_transaction == "waiting_confirm_admin":
            self.bot.send_message(self.message.chat.id,
                                  text="xndrum enq spasel minch admin@ khastati dzer ktron@")
            skip = False
            return skip

        elif state_transaction == "waiting_service_check_number":

            self.bot.send_message(self.message.chat.id,
                                  text=F"der poxancum@ @ntacqi mech e xndrum enq spasel")
            skip = False
            return skip

        elif state_transaction == "waiting_user_wallet_number":
            self.bot.send_message(self.message.chat.id,
                                  text="xndrum enq spasel minch admin@ khastati dzer ktron@")
            skip = False
            return skip

        elif state_transaction == "waiting_choose_wallet":
            self.bot.send_message(self.message.chat.id,
                                  text="xndrum enq spasel minch admin@ khastati dzer ktron@")
            skip = False
            return skip

        elif state_transaction == "success":
            skip = False
            return skip
