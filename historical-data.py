# You have to install modules ib_insync, tzdata, pandas for execute the code
from ib_insync import IB, Forex, util, Order

# Create an instance of the IB class
ib = IB()

# Connect to TWS or IB Gateway
ib.connect('127.0.0.1', 7497, clientId=0)

# Create a Forex contract for EUR/USD
contract = Forex('EURUSD')

# Historical data request
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# Convert historical data to a pandas DataFrame
df = util.df(bars)
print(df)  
