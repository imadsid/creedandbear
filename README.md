**creedandbear**

Python Script that establishes a real-time connection to the Binance WebSocket to capture and process the prices of selected cryptocurrencies

**Prerequisites:**

Python 3.7

**Installation steps**

	1	Clone the repo git clone https://github.com/imadsid41/creedandbear
	2	Create a virtual environment python -m venv venv
	3	Activate the virtual environment source venv/bin/activate
	4	Install the dependencies as specified in the requirements.txt file or use pip install -r requirements.txt
	5	Run the velow scripts: python store_binance_data.py python main.py

**Explaination**

Executing store_binance_data.py script will create web socket connection using Binance API and store the realtime data into the database.

Running main.py script will execute the API server and the APIs will be hosted in the localhost with the port number 8000 i.e. http://127.0.0.1:8000/

After the above scripts are executed, the RESTful APIs needs to be invoked.

Executing test.py will execute the unit tests as requested in the assesment document.
