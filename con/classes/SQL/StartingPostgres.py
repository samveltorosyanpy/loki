from con.classes.SQL.tables.TransactionData import TransactionData
from con.classes.SQL.tables.conf.config import Base, engine, Session
from con.classes.SQL.tables.Transactions import TransactionExchange
from con.classes.SQL.tables.AdminInfo import ChangeInformation
from con.classes.SQL.tables.TranslateTable import Translate
from con.classes.SQL.tables.Users import TelegramUser

Base.metadata.create_all(engine)

Text = Translate()
Data = TransactionData()
UserTable = TelegramUser()
Information = ChangeInformation()
Transaction = TransactionExchange()

Sessions = Session()

