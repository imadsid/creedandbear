import os
import websocket as wb
import json
from binance.client import Client
import pandas as pd
from datetime import datetime
from database_insert import create_table
from base_sql import Session
from trading_data import TradingPrice
from binance_api import get_crypto_currencies

sym = get_crypto_currencies()
sym = [i.lower() + '@kline_1m' for i in sym]
sym_param = '/'.join(sym)
#create the table
create_table()
# create a new session
session = Session()
socket = "wss://stream.binance.com:9443/stream?streams="+sym_param


def on_error(ws, error):
    print(error)

def binance_data(data):
    data_dict = data['data']['k']
    price = data_dict['c']
    sym = data_dict['s']
    # time = pd.to_datetime([data['data']['E']],unit='ms').strftime('%Y-%m-%d %H:%M:%S')
    binance_data_obj = TradingPrice(name=sym, price=price,time=datetime.utcnow())
    try:
        session.add(binance_data_obj)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    session.close()
    return

def on_message(ws,message):
    json_message = json.loads(message)
    binance_data(json_message)


ws = wb.WebSocketApp(socket, on_error=on_error, on_message=on_message)
ws.run_forever()
