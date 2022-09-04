from con.classes.SQL.tables.Transactions import *
from loguru import logger

Sessions = Session()

class TransactionPhoto(Base):
  __tablename__ = 'transaction_photos'

  photo_id = Column(Integer, nullable=False, primary_key=True)
  client_check_image_id = Column(String(250), nullable=True)
  service_check_index = Column(String(250), nullable=True)
  transaction_id = Column(Integer, ForeignKey("transaction_exchanges.transaction_id"), nullable=True)


  def InsertTransactionPhoto(self, value, user_id):
    transaction_id = TransactionExchange().TransactionLastId(user_id)
    Sessions.add(TransactionPhoto(client_check_image_id=str(value['client_check_image_id']), transaction_id=int(transaction_id)))
    Sessions.commit()
    Sessions.close()
    logger.debug(f"User id [{user_id}] | Update the table transaction_photo {value}")

  def ValueUpdate(self, value, id):
    transaction_id = TransactionExchange().TransactionLastId(id)
    Sessions.query(TransactionPhoto).filter(TransactionPhoto.transaction_id == transaction_id).update(value)
    Sessions.commit()
    Sessions.close()
    logger.debug(f"User id [{id}] | Update the table transaction_photo {value}")

