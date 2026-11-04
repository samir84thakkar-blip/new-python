class Computer:
    def __init__(self):
        self.__maxprice = 837
    def sell(self):
        print("Verkaufen Preis:{}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

n = Computer()
n.sell()

n.__maxprice = 999.99
n.sell()


n.setMaxPrice(999.99)
n.sell()

