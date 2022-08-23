from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("postgres://urfelmrraawjmv:56fe7c20b0ca3768ec926f34a7a3ef47fed1e1e9d3029398fe3c640a148e1b50@ec2-52-49-120-150.eu-west-1.compute.amazonaws.com:5432/d1n5sd95rreaum")

Session = sessionmaker(bind=engine)

