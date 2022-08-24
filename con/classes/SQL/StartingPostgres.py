from con.classes.SQL.tables.TransactionIsNotPhoto import TransactionIsNotPhoto
from con.classes.SQL.tables.TransactionPhotos import TransactionPhoto
from con.classes.SQL.tables.conf.config import Base, engine, Session
from con.classes.SQL.tables.Transactions import TransactionExchange
from con.classes.SQL.tables.AdminInfo import ChangeInformation
from con.classes.SQL.tables.Users import TelegramUser

Base.metadata.create_all(engine)

Photo = TransactionPhoto()
UserTable = TelegramUser()
Information = ChangeInformation()
NotPhoto = TransactionIsNotPhoto()
Transaction = TransactionExchange()

Sessions = Session()
