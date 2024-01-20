from ib_insync import IB, Stock, util

# Create an instance of the IB class
ib = IB()

# Connect to TWS or IB Gateway
ib.connect('127.0.0.1', 7497, clientId=0)

# Define the underlying asset (e.g., stock symbol)
underlying_symbol = 'AAPL'

# Create a Stock contract for the underlying asset
stock = Stock(underlying_symbol, 'SMART', 'USD')

# Qualify the stock contract (ensures it is valid and retrieves additional contract details)
ib.qualifyContracts(stock)

# Pause for a short time (1 second) to allow for contract qualification
ib.sleep(1)

# Request option chain parameters for the stock
chains = ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)

# Print the option chain parameters as a DataFrame using util.df
print(util.df(chains))

# Disconnect from TWS or IB Gateway
ib.disconnect()
