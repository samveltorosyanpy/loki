from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, BOOLEAN
from run_test_loki.con.classes.SQL.tables.conf.config import Base, Session
from loguru import logger

Sessions = Session()


class TransactionExchange(Base):
    __tablename__ = 'transaction_exchanges'

    transaction_id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    amount_user = Column(Float, nullable=True)
    amd_amount_pr = Column(Float, nullable=True)
    curacy = Column(String(250), nullable=True)
    amount_crypto = Column(Float, nullable=True)
    amount_crypto_pr = Column(Float, nullable=True)
    cryptocoin = Column(String(250), nullable=True)
    type_transaction = Column(String(250), nullable=True)
    pr_read = Column(BOOLEAN, nullable=True, default=False)
    owner_wallet = Column(String(250), nullable=True)
    user_wallet = Column(String(250), nullable=True)
    armenian_wallet = Column(String(250), nullable=True)
    state_transaction = Column(String(250), nullable=True)
    datetime = Column(DateTime, nullable=True)
    admin_id = Column(Integer, ForeignKey('telegram_users.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('telegram_users.id'), nullable=True)

    def InsertTransactionPending(self, cryptocoin, state_transaction, user_id, admin_id):

        if state_transaction == "success" or state_transaction is None:
            Sessions.add(
                TransactionExchange(cryptocoin=str(cryptocoin), state_transaction="start_transaction",
                                    user_id=int(user_id),
                                    admin_id=admin_id))
            Sessions.commit()
            Sessions.close()
        else:
            pass

    def TransactionLastId(self, id):
        try:
            last_id = list(
                Sessions.query(TransactionExchange.transaction_id).filter(TransactionExchange.user_id == id).order_by(
                    TransactionExchange.transaction_id.desc()).first())[-1]
            return last_id
        except TypeError as ex:
            return 1

    def ValueUpdate(self, value, id):
        transaction_id = TransactionExchange().TransactionLastId(id)
        Sessions.query(TransactionExchange).filter(TransactionExchange.transaction_id == transaction_id).update(value)
        Sessions.commit()
        Sessions.close()
        logger.debug(f"User id [{id}] | Update the table transaction_exchanges {value}")

    # def Dellet(self, user_id):

    def ChackStatus(self, user_id):
        state_transaction = Sessions.query(TransactionExchange.state_transaction).filter(
            TransactionExchange.transaction_id == TransactionExchange().TransactionLastId(id=user_id))[0][0]
        if state_transaction != "success":
            return False

