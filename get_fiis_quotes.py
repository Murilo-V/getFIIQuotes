import investpy as inv
import pandas as pd

country = 'brazil'
lstFIIs = ['KNRI11', 'HGBS11', 'HGLG11', 'MXRF11', 'HGRE11', 'XPLG11']
dictFIIs = {'Ticker': [], 'Fechamento Anterior': [], 'Div. Yield': [], 'Variação 1 ano': []}
for fii in lstFIIs:
    res = inv.stocks.get_stock_information(fii, country, True)
    dictFIIs['Ticker'].append(res['Stock Symbol'])
    dictFIIs['Fechamento Anterior'].append(res['Prev. Close'])
    dictFIIs['Div. Yield'].append(res['Dividend (Yield)'])
    dictFIIs['Variação 1 ano'].append(res['1-Year Change'])
  
dfFIIs = pd.DataFrame(dictFIIs)
print(dfFIIs)
