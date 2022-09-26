from tables.TransactionData import TransactionData
from tables.conf.config import Base, engine, Session
from tables.Transactions import TransactionExchange
from tables.AdminInfo import ChangeInformation
from tables.TranslateTable import Translate
from tables.Users import TelegramUser

Base.metadata.create_all(engine)

Text = Translate()
Data = TransactionData()
UserTable = TelegramUser()
Information = ChangeInformation()
Transaction = TransactionExchange()

Sessions = Session()

