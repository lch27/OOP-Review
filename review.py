class Item:
    pay_rate = 0.8 #the pay rate after 20% discount.
    all = []
    def __init__(self, name: str, price: int, quantity = 0):
        #run validations to the received arguments
        assert price >= 0, f"Price  {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity  {quantity} is not greater than or equal to zero"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}',)"

#Instances
item1 = Item("Chocolate Cake", 14, 2)
item2 = Item("Watermelon Juice", 9, 3)
item3 = Item("Strawberry Cake", 16, 8)
item4 = Item("Egg Tart", 3, 44)
item5 = Item("Chocolate Milk Shake", 6, 35)

print(Item.all)

for instance in Item.all:
    print(instance.name)


