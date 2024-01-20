# You have to install modules ib_insync, tzdata, pandas for execute the code
from ib_insync import IB, Forex, util

# Define a callback function for pending tickers
def onPendingTicker(ticker):
    print("Pending ticker event received")
    print(ticker)

# Create an instance of the IB class
ib = IB()

# Connect to TWS or IB Gateway
ib.connect('127.0.0.1', 7497, clientId=0)

# Create a Forex contract for EUR/USD
contract = Forex('EURUSD')

# Market data request
market_data = ib.reqMktData(contract, '', False, False)

# Ensure market data is received before continuing
ib.waitOnUpdate()

# Print market data
print(market_data)

# Register the callback function for pending tickers
ib.pendingTickersEvent += onPendingTicker

# Sleep for a while to allow time for the pending ticker event
ib.sleep(10)

# Disconnect from TWS or IB Gateway
ib.disconnect()
