# Lorenzo Gonzales
# ID: 1934789
# Zylabs: 10.19 CIS 2348 LAB*: Program: Online shopping cart (Part 2)
class ItemToPurchase :

    def __init__(self, item_name='none', item_price=0, item_quantity=0, string = 'none') :
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.string = string

    def print_item_cost(self, item_cost) :
        print(self.item_name, self.item_quantity, '@', self.item_price, '=', self.item_cost)

    def item_description():



    def print_item_description():
        print('')

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

class ShoppingCart:
    def __init__(self, current_customer = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.current_customer = current_customer
        self.current_date = current_date
        self.cart_items = cart_items
    def add_item(ItemToPurchase):

    def remove_item():
        if:
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(ItemToPurchase):
        if:
        else:
            print('Item not found in cart.Nothing modified.')

    def get_num_items_in_cart():
        return

    def get_cost_of_cart():
        return

    def print_total():
        if:
        else:
            print('SHOPPING CART IS EMPTY')

    def print_descriptions():
        print('')

Main_shop = ShoppingCart()
print('Enter customers name:')
Main_shop.current_customer = input()
Main_shop.current_date =
print('Enter today date:')
Main_shop.
print('Customer name:')

print('Today''s date:')

print('MENU')
print('a - Add item to cart')
print('r - Remove item from cart')
print('c - Change item quantity')
print('i - Output items descriptions')
print('o - Output shopping cart')
print('q - Quit')
print('Choose an option:')