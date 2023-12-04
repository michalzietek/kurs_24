from math import pi
from abc import ABC

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def calculate_price_with_discount(self, discount_type):
#         if discount_type == "black-friday":
#             self.price = self.price * 0.80
#         elif discount_type == "cyber-monday":
#             self.price = self.price * 0.85
#         elif discount_type == "super-customer":
#             self.price = self.price * 0.90
#         else:
#             pass
#
#
# class Product2:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def calculate_price(self):
#         return self.price
#
#
# class BlackFridayProduct(Product2):
#
#     def calculate_price(self):
#         return self.price * 0.8
#
#
# class BlueMondayProduct(Product2):
#
#     def calculate_price(self):
#         return self.price * 0.85
#
#
#
# shop = [Product(name="iphone", price=3000), Product(name="tv", price=2500)]
# chart = [shop[0], shop[1]]
# user = "super-customer"
# if user == "super-customer":
#     for product in chart:
#         product.calculate_price_with_discount("super-customer")


class Shape(ABC):

    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.name = "triangle"
        self.width = width

    def area(self):
        return (self.width * self.height) / 2


class Rectangle(Shape):
    def __init__(self, side):
        self.side = side
        self.name = "rectangle"

    def area(self):
        return (self.side ** 2)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "name"

    def area(self):
        return (pi*self.radius**2)


shapes = [Rectangle(20), Triangle(20, 10), Circle(radius=10)]


def calculate_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area() #powierzchnia części
    print(total_area)


calculate_area(shapes)