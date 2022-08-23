from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("postgresql://postgres:postgres@localhost:5432/bot")

Session = sessionmaker(bind=engine)

