from run_test_loki.con.classes.SQL.tables.TransactionData import TransactionData
from run_test_loki.con.classes.SQL.tables.conf.config import Base, engine, Session
from run_test_loki.con.classes.SQL.tables.Transactions import TransactionExchange
from run_test_loki.con.classes.SQL.tables.AdminInfo import ChangeInformation
from run_test_loki.con.classes.SQL.tables.TranslateTable import Translate
from run_test_loki.con.classes.SQL.tables.Users import TelegramUser

Base.metadata.create_all(engine)

Text = Translate()
Data = TransactionData()
UserTable = TelegramUser()
Information = ChangeInformation()
Transaction = TransactionExchange()

Sessions = Session()
