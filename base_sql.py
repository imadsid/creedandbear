import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine('sqlite:///binance.db',echo=True)
engine.connect()

pprint(f"connection successful! : {engine}")
# create a session variable.
Session = sessionmaker(bind=engine)

Base = declarative_base()

