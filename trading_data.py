# trading_data_sql.py
from sqlalchemy import Date, Column, Integer, String, Float, DateTime

from base_sql import Base

class TradingPrice(Base):
    __tablename__ = "binance"

    id = Column(Integer, primary_key=True)
    name = Column(String(90))
    price = Column(Float())
    time = Column(DateTime())

    def __int__(self, name, price,time):
        self.name = name
        self.price = price
        self.time = time