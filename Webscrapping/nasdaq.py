import requests
from bs4 import BeautifulSoup 
import csv
import pandas as pd

#mostActiveStocksUrl = "https://www.nasdaq.com/markets/most-active.aspx"
r= requests.get("https://www.nasdaq.com/market-activity/stocks/screener")
data=r.text
soup=BeautifulSoup(data)

table=soup.find_all('tbody', attrs={"class":"most-active__body"})
all_rows=table[1].find_all('tr')

symbols=[]
names=[]
last_sales=[]
change_nets=[]
share_volumes=[]

for row in all_rows:
    cols=row.find_all('td')
    if(len(cols)):
        names.append(cols[1].text)
        last_sales.append(cols[2].text)
        change_nets.append(cols[3].text)
        share_volumes.append(cols[4].text)

        
data=pd.DataFrame({"Names":names,"Last Sale": last_sales,"Change Net": change_nets,"Share Volume": share_volumes})


print(data)
