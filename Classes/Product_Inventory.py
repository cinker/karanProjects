#!/usr/bin/python3

# Product Inventory Project - Create an application which manages an inventory
# of products. Create a product class which has a price, id, and quantity on
# hand.
# Then create an inventory class which keeps track of various products and can
# sum up the inventory value.


class Product:
    def __init__(self, prd_price, prd_id, prd_quatity):
        self.prd_id = prd_id
        self.prd_price = prd_price
        self.prd_quatity = prd_quatity

    def get_value(self, prd_id):
        self.prd_value = self.prd_price*self.prd_quatity
        return self.prd_value


class Inventory:
    def __init__(self):
        self.list_prd = []

    def add_product(self, prd_id):
        self.list_prd.append(prd_id)

    def del_product(self, prd_id):
        if prd_id in self.list_prd:
            self.list_prd.remove(prd_id)
        else:
            print("The product is not in the inventory.")

    # TODO: How to calucate this???

    def get_value(self):
        total_value = 0
        for p in self.list_prd:
            total_value += Product.get_value(p)
        return total_value

    def view_inventory(self):
        print(self.list_prd)


p = Product(5, 4, 5)
i = Inventory()
i.add_product(4)
i.get_value()
