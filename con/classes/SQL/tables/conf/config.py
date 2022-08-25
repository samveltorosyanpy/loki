import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

Base = declarative_base()

# SQLALCHEMY_DATABASE_URI = f"postgres://{os.environ['NAME']}:{os.environ['PASSWORD']}@{os.environ['HOST']}:{os.environ['PORT']}/{os.environ['DATABASE']}"

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)

