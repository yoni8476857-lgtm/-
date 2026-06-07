import streamlit as st
from ib_insync import *

st.title("📊 דשבורד נוסטרו אישי")

# חיבור ל-TWS
ib = IB()
try:
    ib.connect('127.0.0.1', 7497, clientId=1)
    contracts = [Stock('AAPL', 'SMART', 'USD'), Forex('EURUSD')]
    ib.qualifyContracts(*contracts)
    ib.reqMarketDataType(3)

    data = []
    for c in contracts:
        ticker = ib.reqMktData(c)
        ib.sleep(0.5)
        price = ticker.marketPrice() if ticker.marketPrice() == ticker.marketPrice() else ticker.last
        data.append({'נכס': c.symbol, 'מחיר': price})

    st.table(data)
    ib.disconnect()
except Exception as e:
    st.error("לא ניתן להתחבר ל-TWS. ודא שהוא פתוח.")
