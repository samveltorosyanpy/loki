from con.classes.Utilites.Utils import *
from con.classes.conf.configuration import *
from con.classes.ApiRequests import ClassApis
from con.classes.SQL.StartingPostgres import *
from con.classes.BigTextsClass import BuySellClass
from con.classes.buttons.button import ButtonsClass


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


class DataWrite():
    def __init__(self):
        pass

    def CurChack(self, bot):

        @bot.message_handler(content_types=['text'])
        def changing_real_time(message):

            user_status = str(Sessions.query(TelegramUser.user_state).filter(TelegramUser.id == message.chat.id)[0][0])

            if user_status == "admin" or user_status == "owner_admin":

                try:

                    user_id = int(str(message.text).split('|')[1])

                    state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                        TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                            user_id))[0][0]
                    type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                        TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                            user_id))[0][0]

                    if state_transaction == "waiting_service_check_number" and type_transaction == "Sell":
                        trx_id = str(message.text).split("|")[0]

                        TransactionData().ValueUpdate(value={"service_check_index": trx_id},
                                                      id=int(user_id))
                        TransactionExchange().ValueUpdate(value={'state_transaction': "success"}, id=user_id)

                        ch = BuySellClass(user_id, type_transaction, bot)
                        bot.send_message(user_id, text=ch.Cack())

                except IndexError as ex:
                    pass

            else:

                curacy = Sessions.query(TransactionExchange.curacy).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(message.chat.id))[0][
                    0]
                cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]
                state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]
                type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]
                pr_read = Sessions.query(TransactionExchange.pr_read).filter(
                    TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                        message.chat.id))[0][0]

                if state_transaction == "waiting_user_amount":

                    slt = isfloat(message.text)

                    while slt == True:

                        amount_exchange = float(message.text)

                        while amount_exchange >= min_limits_amount_exchange[curacy] and amount_exchange <= \
                                max_limits_amount_exchange[curacy]:

                            amount_user = message.text

                            Exchange = ClassApis([cryptocoin])
                            amd_amount_pr, amount_crypto_pr, amount_crypto = Exchange.crypto_price_user(curacy=curacy,
                                                                                                        amount_user=amount_user, pr_read=pr_read, type=type_transaction)

                            type_transaction = Sessions.query(TransactionExchange.type_transaction).filter(
                                TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(
                                    message.chat.id))[0][0]

                            update_value = {
                                "amount_user": float(amount_user),
                                "amount_crypto": float(amount_crypto),
                                "amd_amount_pr": float(amd_amount_pr),
                                "amount_crypto_pr": float(amount_crypto_pr),
                                "state_transaction": f'waiting_user_wallet',
                                'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }

                            TransactionExchange().ValueUpdate(value=update_value, id=message.chat.id)

                            if type_transaction == "Buy":

                                bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 19),
                                                 reply_markup=ButtonsClass().MarkupChoosWallet())

                            elif type_transaction == "Sell":
                                owner_wallet = BnanceApi(cryptocoin).address

                                Transaction.ValueUpdate(
                                    value={"state_transaction": "waiting_user_send_id", "owner_wallet": owner_wallet},
                                    id=message.chat.id)

                                crypto_check = BuySellClass(message.chat.id, "Sell", bot)
                                crypto_check.InformationSendMany(message)

                                ClassMCH = DataWrite()
                                ClassMCH.CurChack(bot)

                            break

                        else:
                            bot.send_message(message.chat.id,
                                             f"{Translate().ShowText(message.chat.id, 20)} {min_limits_amount_exchange[curacy]} {Translate().ShowText(message.chat.id, 34)} {max_limits_amount_exchange[curacy]}")

                            break

                        break


                    else:
                        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 21))

                elif state_transaction == "waiting_user_send_id":

                    Transaction.ValueUpdate({'state_transaction': "waiting_confirm_admin"},
                                            id=message.chat.id)
                    TransactionData().InsertTransactionPhoto(time_interval=None, client_check_image_id=message.text, transaction_id=Transaction.TransactionLastId(message.chat.id))



                    admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

                    bot.send_message(admin_id, text=f"URL: {message.text}")
                    bot.send_message(admin_id, text=Translate().ShowText(admin_id, 33), reply_markup=ButtonsClass().MarkupConfirm(message))

                if state_transaction == "waiting_user_wallet_number":

                    TransactionExchange().ValueUpdate(
                        value={'user_wallet': message.text, "state_transaction": "waiting_service_check_number"},
                        id=message.chat.id)

                    admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]
                    user_wallet = Sessions.query(TransactionExchange.user_wallet).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]
                    armenian_wallet = Sessions.query(TransactionExchange.armenian_wallet).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]
                    cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
                        TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[0][0]

                    if type_transaction == "Buy":

                        bot.send_message(admin_id, text=f"|{message.chat.id}")
                        bot.send_message(admin_id, text=f"{cryptocoin} {message.text}")


                        bot.send_message(admin_id, text=Translate().ShowText(admin_id, 35), reply_markup=ButtonsClass().MarkupSend(message))




                    elif type_transaction == "Sell":

                        bot.send_message(admin_id, text=f"|{message.chat.id}")
                        bot.send_message(admin_id, text=f"""
{Translate().ShowText(admin_id, 36)} {user_wallet} {armenian_wallet}
{Translate().ShowText(admin_id, 35)}
""",
                                         )

                elif state_transaction == 'waiting_manual_time':

                    time_s = message.text

                    try:

                        time1 = bool(datetime.strptime(time_s.split('-')[0], "%H:%M").strftime("%H:%M"))
                        time2 = bool(datetime.strptime(time_s.split('-')[1], "%H:%M").strftime("%H:%M"))

                    except:

                        time1 = False
                        time2 = False

                    while time1 == True or time2 == True:

                        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 29))

                        TransactionExchange().ValueUpdate(
                            value={"state_transaction": "waiting_manual_amount"},
                            id=message.chat.id)

                        transaction_id = TransactionExchange().TransactionLastId(message.chat.id)
                        TransactionData().InsertTransactionPhoto(time_interval=message.text, client_check_image_id=None, transaction_id=int(transaction_id))

                        break

                    else:

                        bot.send_message(message.chat.id,
                                         text=F"{Translate().ShowText(message.chat.id, 30)} '20:00-20:30'")

                elif state_transaction == "waiting_manual_amount":

                    slt = isfloat(message.text)
                    while slt == True:

                        amount_exchange = float(message.text)

                        while amount_exchange >= min_limits_amount_exchange["AMD"] and amount_exchange <= \
                                max_limits_amount_exchange["AMD"]:

                            time_interval = Sessions.query(TransactionData.time_interval).filter(
                                TransactionData.transaction_id == TransactionExchange().TransactionLastId(
                                    message.chat.id))[0][0]

                            TransactionData().ValueUpdate(value={"amount": message.text}, id=message.chat.id)

                            Transaction.ValueUpdate(
                                value={"state_transaction": "waiting_confirm_admin"},
                                id=message.chat.id)

                            admin_id = Sessions.query(TransactionExchange.admin_id).filter(
                                TransactionExchange.transaction_id == Transaction.TransactionLastId(message.chat.id))[
                                0][0]

                            bot.send_message(admin_id, text=f"""
amount-{message.text}
time interval-{time_interval}
""")
                            bot.send_message(admin_id, text=Translate().ShowText(admin_id, 31),
                                             reply_markup=ButtonsClass().MarkupConfirm(message))

                            break

                        else:

                            bot.send_message(message.chat.id,
                                             f"{Translate().ShowText(message.chat.id, 20)} {min_limits_amount_exchange['AMD']} {Translate().ShowText(message.chat.id, 34)} {max_limits_amount_exchange['AMD']}")

                            break

                        break

                    else:

                        bot.send_message(message.chat.id, text=Translate().ShowText(message.chat.id, 21))





