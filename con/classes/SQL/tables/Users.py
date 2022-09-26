from sqlalchemy import Column, Integer, String
from con.classes.SQL.tables.conf.config import Base, Session
from loguru import logger

Sessions = Session()

class TelegramUser(Base):
  __tablename__ = 'telegram_users'

  id = Column(Integer, primary_key=True, nullable=True)
  user_name = Column(String(250), nullable=True)
  language = Column(String(250), nullable=True)
  user_state = Column(String(250), nullable=True)
  # Transaction = relationship('TransactionExchange')

  def InsertUser(self, id, user_name, language, user_state):
    try:
      user = list(Sessions.query(TelegramUser.id).filter(TelegramUser.id == id))[0][0]
      logger.debug(f"User [{id}] is exist in db")
    except IndexError as ex:

      user_state = "owner_admin" if id == 1357108258 else "client"

      logger.debug(f"Add the now user in telegram_users table, Insert the value id={id}, user_name={user_name}")
      Sessions.add(TelegramUser(id=int(id), user_name=user_name, language=language, user_state=user_state))
      Sessions.commit()
      Sessions.close()

      logger.debug(f"User [{id}] is start transaction")

# test = TelegramUser()
# test.InsertUser(id=1259401295, user_name="username", language="russian", user_state="client")