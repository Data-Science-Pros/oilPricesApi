import requests
import pandas as pd
import json 

url = 'https://api.oilpriceapi.com/v1/prices/past_month'

headers = {
  'Authorization': 'Token 0b9b54af3fda3b0c06415f4ab736fb30',
  'Content-Type': 'application/json'
}

response = requests.get(url = url, headers = headers)
responseData = response.json()
priceData = responseData['data']['prices']

priceObject = str(priceData[0])

for i in range(1,len(priceData)):
  priceObject += ',' + str(priceData[i]) 

# print(priceObject)
# print(priceData)

with open('tmp/oilPrices2020.json', 'w') as f:
  json.dump(priceObject, f)