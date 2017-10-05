




class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status


    def display_info(self):
        print("Item: {}".format(self.item_name))
        print("Price: {}".format(self.price))
        print("Weight: {}".format(self.weight))
        print("Brand: {}".format(self.brand))
        print("Cost: {}".format(self.cost))
        print("Status: {}".format(self.status))
        return self


    def sell(self):
        self.status = "sold"
        return self



    def add_tax(self, tax):
        plus_tax = self.price*tax
        print("Price w/tax: ${}".format(plus_tax))
        return self


    def returns(self, reason):
        if "defective" in reason:
            self.status = "defective"
            self.price = 0
            print("The item is defective.")
        elif "still in box" in reason:
            self.status = "for sale"
            print('returned item is has not been opened. Status updated to "for sale"')
        elif "opened" in reason:
            self.status = "used"
            self.price  *= .20
            print("Returned item has been opened. A 20% discount has been applied.")
        return self



class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        products += product

        return self
    
    def remove_product(self, product):
        self.products.remove(product)
        return self

    def inventory(self):
        print("You have {} items in your inventory.".format(len(self.products)))
        for i in products:
            print("{}".format(i.display_info))

        return self
