from sqlalchemy import select
from base_sql import Session
from trading_data import TradingPrice
from binance.client import Client
from sqlalchemy import desc, text, func
import datetime
import statistics

session = Session()

def get_price(currency):
    currency = str(currency).upper()
    try:
        trading_data = session.query(TradingPrice).filter(TradingPrice.name == currency).order_by(
            TradingPrice.time.desc())
        count = trading_data.count()
        if count > 0:
            x = [col.name for col in TradingPrice.__table__.columns]
            trading_data_serialized = []
            for data in trading_data:
                this_trading_data = {}
                for field in x:
                    this_trading_data[field] = getattr(data, field)
                trading_data_serialized.append(this_trading_data)
            return trading_data_serialized
        else:
            return 'No rows found'
    except Exception as Ex:
        return 'Exception'

def get_historical_crypto_data(start,end):
    try:
        trading_data = session.query(TradingPrice).filter(TradingPrice.time > start, TradingPrice.time < end).order_by(
            TradingPrice.time.desc())
        count = trading_data.count()
        if count > 0:
            x = [col.name for col in TradingPrice.__table__.columns]
            trading_data_serialized = []
            for data in trading_data:
                this_trading_data = {}
                for field in x:
                    this_trading_data[field] = getattr(data, field)
                trading_data_serialized.append(this_trading_data)
            return trading_data_serialized
        else:
            return 'No rows found'
    except Exception as Ex:
        return 'Exception'

def get_statistical_analysis(currency):
    price_list = []
    data_dict = {}
    data_list = []
    percentage_change = {}
    try:
        trading_data = get_price(currency)
        if trading_data == 'Exception' or trading_data == 'No rows found':
            return 'No rows found'
        else:
            for i in trading_data:
                price_list.append(i['price'])
            avg_value = round(statistics.mean(price_list),4)
            median = round(statistics.median(price_list),4)
            standard_deviation = round(statistics.stdev(price_list),4)
            percentage_change[price_list[0]] = 0
            for a, b in zip(price_list[::1], price_list[1::1]):
                percentage_change[a + 1] = round((100 * (b - a) / a), 2)
            data_dict['currency'] = currency
            data_dict['average'] = avg_value
            data_dict['median'] = median
            data_dict['standard_deviation'] = standard_deviation
            data_dict['percentage_change'] = percentage_change
            return data_dict
    except Exception as Ex:
        return 'Exception'

def get_crypto_currencies():
    try:
        client = Client()
        dict = client.get_exchange_info()
        sym = [i['symbol'] for i in dict['symbols'] if i['symbol'].endswith('USDT')]
        return sym[:6]
    except Exception as Ex:
        return 'Exception'


