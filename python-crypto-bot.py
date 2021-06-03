import os
import hmac
import hashlib
import base64
import json
import time
import requests


key = os.environ.get('KEY')
secret = os.environ.get('SIGNATURE') 

secret_bytes = bytes(secret, encoding='utf-8')

timeStamp = int(round(time.time() * 1000))

#CREATE THE ORDER

body = {
    "side": "buy",  .
  "order_type": "limit_order",
  "market": "BTCUSDT", 
  "price_per_unit": 42342.89, 
  "total_quantity": 0.002, 
  "timestamp": timeStamp
}

json_body = json.dumps(body, separators = (',', ':'))

signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

url = "https://api.coindcx.com/exchange/v1/orders/create"

headers = {
    'Content-Type': 'application/json',
    'X-AUTH-APIKEY': key,
    'X-AUTH-SIGNATURE': signature
}

response = requests.post(url, data = json_body, headers = headers)
data = response.json()


#CHECK BALANCE
url = "https://api.coindcx.com/exchange/v1/users/balances"
response = requests.post(url, data = json_body, headers = headers)
data = response.json();
print(data);

#CANCEL ALL ORDERS IRRESPECTIVE
url="https://api.coindcx.com/exchange/v1/orders/cancel_all"
response = requests.post(url, data = json_body, headers = headers)
data = response.json();
print(data);

