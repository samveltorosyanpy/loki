# from sqlalchemy import Column, Integer, String, ForeignKey
# from con.classes.SQL.tables.conf.config import *
# from con.classes.conf.configuration import *
from con.classes.SQL.tables.Transactions import *
from loguru import logger

Sessions = Session()

class TransactionIsNotPhoto(Base):
  __tablename__ = 'transaction_is_not_photo'

  chack_id = Column(Integer, nullable=False, primary_key=True)
  time_interval = Column(String(250), nullable=True)
  amount = Column(String(250), nullable=True)
  transaction_id = Column(Integer, ForeignKey("transaction_exchanges.transaction_id"), nullable=True)

  def InsertTransactionChackInfo(self, value, user_id):
    transaction_id = TransactionExchange().TransactionLastId(user_id)
    Sessions.add(TransactionIsNotPhoto(time_interval=str(value['time_interval']), transaction_id=int(transaction_id)))
    Sessions.commit()
    Sessions.close()
    logger.debug(f"User id [{user_id}] | Update the table transaction_is_not_photo {value}")

  def ValueUpdate(self, value, id):
    transaction_id = TransactionExchange().TransactionLastId(id)
    Sessions.query(TransactionIsNotPhoto).filter(TransactionIsNotPhoto.transaction_id == transaction_id).update(value)
    Sessions.commit()
    Sessions.close()
    logger.debug(f"User id [{id}] | Update the table transaction_is_not_photo {value}")

