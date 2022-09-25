from con.classes.SQL.tables.Users import *

Sessions = Session()

class Translate(Base):
    __tablename__ = 'Translates'

    id = Column(Integer, nullable=False, primary_key=True)
    armenian = Column(String(250), nullable=True)
    russian = Column(String(250), nullable=True)
    english = Column(String(250), nullable=True)

    def ShowText(self, user_id, text_id):
        try:
            language = Sessions.query(TelegramUser.language).filter(TelegramUser.id == user_id)[0][0]
        except IndexError as ex:
            language = None
        if language == "armenian":
            text = Sessions.query(Translate.armenian).filter(Translate.id == text_id)[0][0]
        elif language == "russian":
            text = Sessions.query(Translate.russian).filter(Translate.id == text_id)[0][0]
        elif language == "english":
            text = Sessions.query(Translate.english).filter(Translate.id == text_id)[0][0]
        return str(text)