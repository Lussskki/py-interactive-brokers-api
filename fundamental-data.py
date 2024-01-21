from ib_insync import IB, Stock
from bs4 import BeautifulSoup as bs
from xml.etree import ElementTree as ET

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=0)

stock = Stock('AAPL', 'SMART', 'USD')



# Specify the report type (e.g., 'ReportSnapshot')
report_type = 'ReportSnapshot'

try:
    # Request fundamental data
    fundamentals = ib.reqFundamentalData(stock, report_type)
    print(fundamentals)
    # Check the type of data returned
    if isinstance(fundamentals, str):
        # Use the lxml parser with features="xml"
        content = bs(fundamentals, "lxml-xml")
    else:
        print(f"Unexpected data type received: {type(fundamentals)}")

except Exception as e:
    print(f"Error retrieving fundamental data: {e}")

finally:
    # Disconnect from TWS or IB Gateway
    ib.disconnect()
