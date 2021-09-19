import json
from os import times

with open('./data.json', 'r') as f:
    data = json.load(f)

name = input('client ')
time = input('time of order ')
result = []

for order in data['db']['orders']:
    if order['client']['name'] == name and order['time'] == time:
        result.append(order)
print(result)