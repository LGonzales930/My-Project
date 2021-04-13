# Lorenzo Gonzales
# ID: 1934789
import csv  # The csv format is imported into the system
# Four separate dictionaries are created categorizing the data in different orders
Inventory_fields_1 = ['ID', 'Manufacture', 'Item type', 'price', 'service date', 'damage_indicator']
# ID, Manufacture, price, service date and damage_indicator are assigned as fields
# The First dictionary is ordered by Manufacture
Inventory_fields_1 = ['ID', 'Manufacture', 'Item type', 'price', 'service date', 'damage_indicator']
Full_Inventory_dict = [
    {'ID': '2347800', 'Manufacture': 'Apple', 'Item type': 'laptop', 'price': '$999', 'service date': '7/3/2020'},
    {'ID': '1167234', 'Manufacture': 'Apple', 'Item type': 'phone', 'price': '$534', 'service date': '2/1/2022'},
    {'ID': '2390112', 'Manufacture': 'Dell', 'Item type': 'laptop', 'price': '$799', 'service date': '7/2/2020'},
    {'ID': '9034210', 'Manufacture': 'Dell', 'Item type': 'tower', 'price': '$345', 'service date': '5/27/2020'},
    {'ID': '7346234', 'Manufacture': 'Lenovo', 'Item type': 'laptop', 'price': '$239', 'service date': '9/1/2021', 'damage_indicator': 'damaged'},
    {'ID': '1009453', 'Manufacture': 'Lenovo', 'Item type': 'tower', 'price': '$599', 'service date': '10/1/2021'},
    {'ID': '3001265', 'Manufacture': 'Samsung', 'Item type': 'phone', 'price': '$1200', 'service date': '12/1/2023'},
]
# Program opens the file and writes in the dictionary giving it fields and rows
with open("../../PycharmProjects/pythonProject13/FullInventory.csv", "w") as full:
    writer_1 = csv.DictWriter(full, fieldnames=Inventory_fields_1)
    writer_1.writeheader()
    writer_1.writerows(Full_Inventory_dict)

Inventory_fields_2 = ['ID', 'Manufacture', 'price', 'service date', 'damage_indicator']
# The Second Dictionary is ordered by ID number
Laptop_Inventory_dict = [
    {'ID': '1009453', 'Manufacture': 'Lenovo', 'price': '599', 'service date': '10/1/2021'},
    {'ID': '1167234', 'Manufacture': 'Apple', 'price': '534', 'service date': '2/1/2022'},
    {'ID': '2347800', 'Manufacture': 'Apple', 'price': '999', 'service date': '7/3/2020'},
    {'ID': '2390112', 'Manufacture': 'Dell', 'price': '799', 'service date': '7/2/2020'},
    {'ID': '3001265', 'Manufacture': 'Samsung', 'price': '1200', 'service date': '12/1/2023'},
    {'ID': '7346234', 'Manufacture': 'Lenovo', 'price': '239', 'service date': '9/1/2021', 'damage_indicator': 'damaged'},
    {'ID': '9034210', 'Manufacture': 'Dell', 'price': '345', 'service date': '5/27/2020'},
]
with open("../../PycharmProjects/pythonProject13/LaptopInventory.csv", "w") as laptop:
    writer_2 = csv.DictWriter(laptop, fieldnames=Inventory_fields_2)
    writer_2.writeheader()
    writer_2.writerows(Laptop_Inventory_dict)

Inventory_fields_3 = ['ID', 'Manufacture', 'Item type', 'price', 'service date', 'damage_indicator']
# The Third Dictionary is ordered from oldest to most recent service date
Past_Service_Inventory_dict = [
    {'ID': '9034210', 'Manufacture': 'Dell', 'Item type': 'tower', 'price': '345', 'service date': '5/27/2020'},
    {'ID': '2390112', 'Manufacture': 'Dell', 'Item type': 'laptop', 'price': '799', 'service date': '7/2/2020'},
    {'ID': '2347800', 'Manufacture': 'Apple', 'Item type': 'laptop', 'price': '999', 'service date': '7/3/2020'},
    {'ID': '7346234', 'Manufacture': 'Lenovo', 'Item type': 'laptop', 'price': '239', 'service date': '9/1/2021', 'damage_indicator': 'damaged'},
    {'ID': '1009453', 'Manufacture': 'Lenovo', 'Item type': 'tower', 'price': '599', 'service date': '10/1/2021'},
    {'ID': '1167234', 'Manufacture': 'Apple', 'Item type': 'phone', 'price': '534', 'service date': '2/1/2022'},
    {'ID': '3001265', 'Manufacture': 'Samsung', 'Item type': 'phone', 'price': '1200', 'service date': '12/1/2023'},
]
with open("../../PycharmProjects/pythonProject13/PastServiceDateInventory.csv", "w") as past:
    writer_3 = csv.DictWriter(past, fieldnames=Inventory_fields_3)
    writer_3.writeheader()
    writer_3.writerows(Past_Service_Inventory_dict)

Inventory_fields_4 = ['ID', 'Manufacture', 'Item type', 'price', 'service date']
# The fourth Dictionary orders the data by price
Damaged_Inventory_dict = [
    {'ID': '3001265', 'Manufacture': 'Samsung', 'Item type': 'phone', 'price': '1200', 'service date': '12/1/2023'},
    {'ID': '2347800', 'Manufacture': 'Apple', 'Item type': 'laptop', 'price': '999', 'service date': '7/3/2020'},
    {'ID': '2390112', 'Manufacture': 'Dell', 'Item type': 'laptop', 'price': '799', 'service date': '7/2/2020'},
    {'ID': '1009453', 'Manufacture': 'Lenovo', 'Item type': 'tower', 'price': '599', 'service date': '10/1/2021'},
    {'ID': '1167234', 'Manufacture': 'Apple', 'Item type': 'phone', 'price': '534', 'service date': '2/1/2022'},
    {'ID': '9034210', 'Manufacture': 'Dell', 'Item type': 'tower', 'price': '345', 'service date': '5/27/2020'},
    {'ID': '7346234', 'Manufacture': 'Lenovo', 'Item type': 'laptop', 'price': '239', 'service date': '9/1/2021'}
]
with open("../../PycharmProjects/pythonProject13/DamagedInventory.csv", "w") as damage:
    writer_4 = csv.DictWriter(damage, fieldnames=Inventory_fields_4)
    writer_4.writeheader()
    writer_4.writerows(Damaged_Inventory_dict)

print('Below is the Inventory listed by Manufacture ')
# The program reads and outputs the first inventory list in order from alphabetical order of manufacture
full = open("../../PycharmProjects/pythonProject13/FullInventory.csv", "r")
file_4 = csv.reader(full)
for i in file_4:
    print(i)

print("------")  # The print of lines is produced to separate outputs of the four files

print('Below is the Inventory listed by ID')
# The program reads and outputs the second inventory in numeric order of ID
laptop = open("../../PycharmProjects/pythonProject13/LaptopInventory.csv", "r")
file_5 = csv.reader(laptop)
for i in file_5:
    print(i)

print("------")
print('Below is the Inventory listed by Service Date ')
# The program reads and outputs the third inventory list in order from oldest to most recent service date
full = open("../../PycharmProjects/pythonProject13/PastServiceDateInventory.csv", "r")
file_6 = csv.reader(full)
for i in file_6:
    print(i)

print("------")
print('Below is the Inventory listed by Price ')
# The Program outputs the fourth dictionary list in order of most to least expensive inventory
damage = open("../../PycharmProjects/pythonProject13/DamagedInventory.csv", "r")
file_7 = csv.reader(damage)
for i in file_7:
    print(i)
