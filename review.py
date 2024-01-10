class Item:
    def calculate_total_price(self, x, y):
        return x * y


#Instances
item1 = Item()
item1.name = "Chocolate Cake"
item1.price = 36
item1.quantity = 10
total_price1 = item1.calculate_total_price(item1.price, item1.quantity)
print(total_price1)

item2 = Item()
item2.name = "Watermelon Juice"
item2.price = 9
item2.quantity = 50
total_price2 = item2.calculate_total_price(item2.price, item2.quantity)
print(total_price2)


# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
