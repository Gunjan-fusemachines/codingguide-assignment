from abc import abstractmethod

class Product:
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_price(self):
        pass


class RegularProduct(Product):
    def get_price(self):
        return self.price


class DiscountProduct(Product):
    def __init__(self, price, discount):
        super().__init__(price)
        self.discount = discount

    def get_price(self):
        return self.price - (self.price * self.discount / 100)


def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.get_price()
    return total_price


# Using the calculate_total_price function with a list of products
products = [RegularProduct(100), DiscountProduct(50, 10), RegularProduct(75)]
print("Total Price:", calculate_total_price(products))
