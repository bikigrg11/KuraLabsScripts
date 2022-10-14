import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price : float, quantity = 0):
        assert price >=0, f"price {price} should be great than or equla to 0"
        assert quantity >=0, f"quantity {quantity} should be great than or equla to 0"
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)


    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,val):
        self.__price= val
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price  + self.__price * increment_value

    
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.__price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/bikigurung/Desktop/KuraLabScripts/Python/OOP/item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity= int(item.get('quantity'))
            )
            # print(item)

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            # Count out the floats that are point zerio
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
             
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value


    
