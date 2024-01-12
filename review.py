class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


#Instances
item1 = Item("Chocolate Cake", 15, 50)

item2 = Item("Watermelon Juice", 9, 30)

print(item1.calculate_total_price())
print(item2.calculate_total_price())