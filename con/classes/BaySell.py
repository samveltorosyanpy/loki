from con.classes.conf.configuration import *



class BaySellClass():
    def __init__(self, user_id, type_transaction):
        self.user_id = user_id
        self.type_transaction = type_transaction

    def InformationSendMany(self):
        cryptocoin = Sessions.query(TransactionExchange.cryptocoin).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        armenian_wallet = Sessions.query(TransactionExchange.armenian_wallet).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        amount_crypto_pr = Sessions.query(TransactionExchange.amount_crypto_pr).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0]
        amd_amount_pr = (Sessions.query(TransactionExchange.amd_amount_pr).filter(
            TransactionExchange.transaction_id == Transaction.TransactionLastId(self.user_id))[0][0])

        if self.type_transaction == 'Bay':
            text = f"""
{Translate().ShowText(self.user_id, 12)}
{Translate().ShowText(self.user_id, 15)} {armenian_wallet} {wallet_data[armenian_wallet.lower()]['wallet_key']}
{Translate().ShowText(self.user_id, 14)} {amd_amount_pr} {cryptocoin}
{Translate().ShowText(self.user_id, 13)}
            """
            return text
        elif self.type_transaction == 'Sell':
            text = f"""
{Translate().ShowText(self.user_id, 12)}
{Translate().ShowText(self.user_id, 15)} {cryptocoin} {wallet_data[cryptocoin.upper()]['wallet_key']}
{Translate().ShowText(self.user_id, 14)} {amount_crypto_pr} {cryptocoin}
{Translate().ShowText(self.user_id, 13)}
            """
            return text


