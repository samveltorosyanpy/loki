from sqlalchemy import Column, Integer, String
from run_test_loki.con.classes.SQL.tables.conf.config import Base, Session
from loguru import logger

Sessions = Session()

class ChangeInformation(Base):
  __tablename__ = 'change_information'

  id = Column(Integer, primary_key=True, nullable=False)
  limit_time_send_photo = Column(Integer, nullable=False)
  commission = Column(Integer, nullable=False)
  amd_price = Column(Integer, nullable=False)
  owner_id = Column(Integer, nullable=False)

  min_limits_amount_exchange_amd = Column(String(250), nullable=False)
  min_limits_amount_exchange_usd = Column(String(250), nullable=False)
  min_limits_amount_exchange_btc = Column(String(250), nullable=False)
  min_limits_amount_exchange_dash = Column(String(250), nullable=False)
  min_limits_amount_exchange_xrp = Column(String(250), nullable=False)
  min_limits_amount_exchange_ltc = Column(String(250), nullable=False)

  max_limits_amount_exchange_amd = Column(String(250), nullable=False)
  max_limits_amount_exchange_usd = Column(String(250), nullable=False)
  max_limits_amount_exchange_btc = Column(String(250), nullable=False)
  max_limits_amount_exchange_dash = Column(String(250), nullable=False)
  max_limits_amount_exchange_xrp = Column(String(250), nullable=False)
  max_limits_amount_exchange_ltc = Column(String(250), nullable=False)

  owner_walet_idram = Column(String(250), nullable=False)
  owner_walet_telcell = Column(String(250), nullable=False)
  owner_walet_easypay = Column(String(250), nullable=False)


  def ValueUpdate(self, value, id):
    transaction_id = ChangeInformation().TransactionLastId(id)
    Sessions.query(ChangeInformation).filter(ChangeInformation.transaction_id == transaction_id).update(value)
    Sessions.commit()
    Sessions.close()
    logger.debug(f"User id [{id}] | Update the table transaction_photo {value}")