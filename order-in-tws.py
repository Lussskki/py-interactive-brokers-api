from ib_insync import IB, Forex, util, Order

# Create an instance of the IB class
ib = IB()

# Connect to TWS or IB Gateway
ib.connect('127.0.0.1', 7497, clientId=0)

# Create a Forex contract for EUR/USD
contract = Forex('EURUSD')

# Place a market order example
order = Order()
order.action = 'BUY'
order.totalQuantity = 10  # Specify the quantity you want to buy
order.orderType = 'MKT'  # Market order type
order.transmit = True  # This ensures that the order is transmitted to the exchange immediately
order.account = 'DU8202250'  # Set the account attribute with your account number

# Place the order
try:
    trade = ib.placeOrder(contract, order)
    print(f"Order placed successfully: {trade}")
except Exception as e:
    print(f"Error placing order: {e}")

# Disconnect from IB
ib.disconnect()
