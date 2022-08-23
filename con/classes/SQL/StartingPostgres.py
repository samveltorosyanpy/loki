from con.classes.SQL.tables.conf.config import Base, engine, Session
from con.classes.SQL.tables.Users import TelegramUser
from con.classes.SQL.tables.Transactions import TransactionExchange
from con.classes.SQL.tables.TransactionPhotos import TransactionPhoto
from con.classes.SQL.tables.TransactionIsNotPhoto import TransactionIsNotPhoto

Base.metadata.create_all(engine)

Photo = TransactionPhoto()
UserTable = TelegramUser()
NotPhoto = TransactionIsNotPhoto()
Transaction = TransactionExchange()

Sessions = Session()
