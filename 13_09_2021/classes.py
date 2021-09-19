class Driver:
    def __init__(self, mark, name, phone, car) -> None:
        self.mark = mark
        self.name = name
        self.phone = phone
        self.car = car

class Client:
    def __init__(self,phone,name, payway) -> None:
        self.phone = phone
        self.name = name
        self.pay_way = payway


class TaksoPark:
    def __init__(self,drivers, cars) -> None:
        self.drivers = drivers
        self.cars = cars

class Order:
    def __init__(self,price,adres,time, client, driver) -> None:
        self.driver = driver
        self.client = client
        self.price = price
        self.adres = adres
        self.time = time

class Car:
    def __init__(self,clas,color,number) -> None:
        self.clas = clas
        self.color = color
        self.number = number
