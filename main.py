import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.worldometers.info/world-population/india-population/#:~:text=The%20current%20population%20of%20India,of%20the%20total%20world%20population."
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
# print(soup)
table=(soup.select("table"))[1]
heading=table.find_all("th")
heading=[i.text.strip() for i in heading]
# print(heading)
row=(table.find_all("tr"))[1:]
df=pd.DataFrame(columns=heading)
print(heading)
for i in row:
    data = i.find_all("td")
    data =[j.text.strip() for j in data]
    l=len(df)
    df.loc[l]=data
df.to_csv('population.csv',index=False)