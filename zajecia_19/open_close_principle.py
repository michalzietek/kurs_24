class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price_with_discount(self, discount_type):
        if discount_type == "black-friday":
            self.price = self.price * 0.80
        elif discount_type == "cyber-monday":
            self.price = self.price * 0.85
        elif discount_type == "super-customer":
            self.price = self.price * 0.90
        else:
            pass


class Product2:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price


class BlackFridayProduct(Product2):

    def calculate_price(self):
        return self.price * 0.8


class BlueMondayProduct(Product2):

    def calculate_price(self):
        return self.price * 0.85



shop = [Product(name="iphone", price=3000), Product(name="tv", price=2500)]
chart = [shop[0], shop[1]]
user = "super-customer"
if user == "super-customer":
    for product in chart:
        product.calculate_price_with_discount("super-customer")