from sqlalchemy import Column, Integer, String, ForeignKey
from con.classes.SQL.tables.conf.config import Base, Session
from con.classes.SQL.tables.Transactions import TransactionExchange
from loguru import logger

Sessions = Session()

class TransactionData(Base):
  __tablename__ = 'transaction_data'

  photo_id = Column(Integer, nullable=False, primary_key=True)
  client_check_image_id = Column(String(250), nullable=True)
  service_check_index = Column(String(250), nullable=True)
  time_interval = Column(String(250), nullable=True)
  amount = Column(String(250), nullable=True)
  transaction_id = Column(Integer, ForeignKey("transaction_exchanges.transaction_id"), nullable=True)


  def InsertTransactionPhoto(self, time_interval, client_check_image_id, transaction_id):
    Sessions.add(TransactionData(time_interval=time_interval, client_check_image_id=client_check_image_id, transaction_id=transaction_id))
    Sessions.commit()
    Sessions.close()

  def ValueUpdate(self, value, id):
    transaction_id = TransactionExchange().TransactionLastId(id)
    Sessions.query(TransactionData).filter(TransactionData.transaction_id == transaction_id).update(value)
    Sessions.commit()
    Sessions.close()
    logger.debug(f"User id [{id}] | Update the table transaction_photo {value}")

