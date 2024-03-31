from flask import Flask, request, jsonify
import subprocess
from binance_api import get_price,get_historical_crypto_data,get_statistical_analysis, get_crypto_currencies
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    data = {'Result':'App loaded successfully','Message':'Success','Status':200}
    return jsonify(data)

@app.route('/get_latest_price/')
def get_latest_price():
    currency = str(request.args.get('currency'))
    dict = {}
    try:
        currency_list = get_crypto_currencies()
        if currency.upper() not in currency_list:
            data_set = {'Result': {}, 'Message': currency + ' is not available. Please use the currencies specified in the API document or invoke "get_currencies" api to get the available list of currencies.', 'Status': 200,'Timestamp': datetime.now()}
            return jsonify(data_set)
        data = get_price(currency)
        if data == 'Exception' or data == 'No rows found':
            data_set= {'Result': {}, 'Message': 'No results found for your query', 'Status': 200, 'Timestamp':datetime.now()}
            return jsonify(data_set)
        else:
            latest_price = data[0]
            dict['Name'] = latest_price['name']
            dict['Price'] = latest_price['price']
            data_set = {'Result': dict, 'Message': 'Success', 'Status': 200, 'Timestamp':datetime.now()}
            return jsonify(data_set)
    except Exception as Ex:
        data_set = {'Result': {}, 'Message': 'No results found for your query', 'Status': 400, 'Timestamp':datetime.now()}
        return jsonify(data_set)

@app.route('/get_statistical_data/')
def get_statistical_data():
    currency = str(request.args.get('currency'))
    dict = {}
    try:
        currency_list = get_crypto_currencies()
        if currency.upper() not in currency_list:
            data_set = {'Result': {}, 'Message': currency + ' is not available. Please use the currencies specified in the API document or invoke "get_currencies" api to get the available list of currencies.', 'Status': 200,'Timestamp': datetime.now()}
            return jsonify(data_set)
        data = get_statistical_analysis(currency)
        if data == 'Exception' or data == 'No rows found':
            data_set= {'Result': {}, 'Message': 'No results found for your query', 'Status': 200, 'Timestamp':datetime.now()}
            return jsonify(data_set)
        else:
            dict['currency'] = data['currency']
            dict['average'] = data['average']
            dict['median'] = data['median']
            dict['standard_deviation'] = data['standard_deviation']
            dict['percentage_change'] = data['percentage_change']
            data_set = {'Result': dict, 'Message': 'Success', 'Status': 200, 'Timestamp':datetime.now()}
            return jsonify(data_set)
    except Exception as Ex:
        data_set = {'Result': {}, 'Message': 'No results found for your query', 'Status': 400, 'Timestamp':datetime.now()}
        return jsonify(data_set)

@app.route('/get_currencies/')
def get_available_currencies():
    try:
        currencies = get_crypto_currencies()
        if currencies == 'Exception':
            data_set = {'Result': {}, 'Message': 'No results found for your query', 'Status': 400, 'Timestamp': datetime.now()}
            return jsonify(data_set)
        else:
            data_set = {'Result': currencies, 'Message': 'Success', 'Status': 200, 'Timestamp': datetime.now()}
            return jsonify(data_set)
    except Exception as Ex:
        data_set = {'Result': {}, 'Message': 'No results found for your query', 'Status': 400,
                    'Timestamp': datetime.now()}
        return jsonify(data_set)

@app.route('/get_historical_data/')
def get_historical_data():
    data_list = []
    try:
        start_time = datetime.strptime(str(request.args.get('start')),'%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(str(request.args.get('end')),'%Y-%m-%d %H:%M:%S')
        initial_storage_time = datetime.strptime('2024-03-30 02:53:02', '%Y-%m-%d %H:%M:%S')
        latest_storage_time = datetime.now()
    except Exception as Ex:
        data_set = {'Result': {}, 'Message': 'Kindly provide the datetime in "YYYY-MM-DD HH:MM:SS" format.', 'Status': 200, 'Timestamp': datetime.now()}
        return jsonify(data_set)
    if start_time < initial_storage_time or end_time > latest_storage_time:
        data_set = {'Result': {}, 'Message': 'Kindly provide the datetime in a range between 2024-03-30 02:53:02 and '+str(datetime.now()),
                    'Status': 200, 'Timestamp': datetime.now()}
        return jsonify(data_set)
    try:
        historical_data = get_historical_crypto_data(start_time,end_time)
        if historical_data == 'Exception' or historical_data == 'No rows found':
            data_set = {'Result': {}, 'Message': 'No results found for your query', 'Status': 200,
                        'Timestamp': datetime.now()}
            return jsonify(data_set)
        else:
            for i in historical_data:
                dict = {}
                dict['Name'] = i['name']
                dict['Price'] = i['price']
                data_list.append(dict)
        data_set = {'Result': data_list, 'Message': 'Success', 'Status': 200, 'Timestamp': datetime.now()}
        return jsonify(data_set)
    except Exception as Ex:
        data_set = {'Result': {}, 'Message': 'No results found for your query', 'Status': 400,
                    'Timestamp': datetime.now()}
        return jsonify(data_set)



if __name__ == "__main__":
    app.run(port=8000)