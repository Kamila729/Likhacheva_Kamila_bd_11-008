import json
from typing import cast
from classes import Car, Client, Driver, Order, TaksoPark
import re


clients = [Client(63748883364, "Angela", 'card'),
           Client(76423479238,"Masha", 'nal')]

cars = [Car("Wolkswaggen","balck", "t 243 hg"),
        Car("Reno","yellow","b 123 gd")]

drivers = [Driver(5,"Vasya", 5683324782, cars[0]),
           Driver(4,"Ludvig", 273846237, cars[1])]


orders = [Order(123,"xxxxxx","21.01.2021 16:40",clients[0], drivers[0]),
          Order(120,"xxxxx1x","43.04.2020 13:25", clients[0], drivers[0])]

db = {
"db" : {
    "clients":list({"phone":client.phone,
                    "name":client.name,
                    'payway':client.pay_way} for client in clients),

    "drivers":list({"mark":driver.mark,
                    "name":driver.name,
                    "phone":driver.phone,
                    'car':{'model':driver.car.clas,
                           'color':driver.car.color,
                           'number':driver.car.number}} for driver in drivers),

    "cars":list({"clas":car.clas,
                 "color":car.color,
                 "number":car.number} for car in cars),

    "orders":list({"price":oder.price,
                   "adres":oder.adres,
                   "time":oder.time,
                   'client':{'phone':oder.client.phone,
                             'name':oder.client.name,
                             'payway':oder.client.pay_way },
                    'driver':{'mark':oder.driver.mark,
                              'name':oder.driver.name,
                              'phone':oder.driver.phone,
                              'car':{'clas':oder.driver.car.clas,
                                     'color':oder.driver.car.color,
                                     'number':oder.driver.car.number}}} for oder in orders),

    
}
}
db['db']["taksopark"] = [db['db']['drivers'],db['db']['clients']]

print(db['db']["taksopark"])
with open('./data.json', 'w', encoding='utf8') as f:
    json.dump(db, f)
