from ib_insync import IB, Stock
from xml.etree import ElementTree as ET

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=0)

stock = Stock('AAPL', 'SMART', 'USD')

fundamentals = ib.reqFundamentalData(stock, 'ReportSnapshot')

# Parse XML data
root = ET.fromstring(fundamentals)

# Now you can navigate through the XML structure using ElementTree methods
# For example, let's print the names of all the child elements of the root
for child in root:
    print(child.tag)

# If you want to extract specific information, you can navigate through the XML structure accordingly
# For example, let's print the value of the 'DocumentTitle' element
document_title = root.find('.//DocumentTitle')
if document_title is not None:
    print('Document Title:', document_title.text)

# Close the connection
ib.disconnect()
