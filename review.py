class Item:
    def __init__(self, name: str, price: int, quantity = 0):
        #run validations to the received arguments
        assert price >= 0, f"Price  {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity  {quantity} is not greater than or equal to zero"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


#Instances
item1 = Item("Chocolate Cake", 14, 2)

item2 = Item("Watermelon Juice", 9, 30)

print(item1.calculate_total_price())
print(item2.calculate_total_price())