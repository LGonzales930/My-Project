# Lorenzo Gonzales
# ID: 1934789
# Zylabs: 10.17 CIS 2348 LAB*: Warm up: Online shopping cart (Part 1)
class ItemToPurchase:

    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', self.item_price, '=')

Item_purchase1 = ItemToPurchase()
print('Item 1')
print('Enter the item name:')
Item_purchase1.item_name = input()
print('Enter the item price:')
Item_purchase1.item_price = int(input())
print('Enter the item quantity:')
Item_purchase1.item_quantity = int(input())
Item_purchase2 = ItemToPurchase
print('Item 2:')
print('Enter the item name:')
Item_purchase2.item_name = input()
print('Enter the item price:')
Item_purchase2.item_price = int(input())
print('Enter the item quantity:')
Item_purchase2.item_quantity = int(input())

print('TOTAL COST:')
print(Item_purchase1.print_item_cost())
print(Item_purchase2.print_item_cost())
Total = Item_purchase1 + Item_purchase2
print('TOTAL:', Total)
