# Lorenzo Gonzales
# ID: 1934789
# Final Project part 2
# The Following program outputs information about an Electronics stores inventory
import csv
# The Dictionary ID is created to connect the other values together as a key, Everything else acts as a value
# Everything is connected using
ID = {}

with open("ManufacturerList.csv", "r") as Info_1:  # Information is read and accessed from the manufacture csv file
    Info_reader_1 = csv.reader(Info_1)
for row in Info_reader_1:
    ID[row[0]] = {'Manufacture': row[1], 'Type': row[2]}


with open("PriceList.csv", "r") as Info_2:  # Information is read and accessed from the Price list csv file
   Info_reader_2 = csv.reader(Info_2)
for row in Info_reader_2:
    ID[row[0]] = {'Price': row[1]}


with open("ServiceDatesList.csv", "r") as Info_3:   # Information is read and accessed from Service Dates List csv file
    Info_reader_3 = csv.reader(Info_3)
for row in Info_reader_3:
    ID[row[0]] = {'Date': row[1]}


print("Greetings User")  # Program greets user and prompts for information
print("Please enter a Manufacture name and Item type to proceed:")
Selection = input()

if 'Manufacture' and 'Type' in ID:
    print("Your item is:", ID['Manufacture': row[1]]['Type': row[2]]['Price': row[1][['Date']: row[1]]])
elif Selection == "q":
    print("Have a Nice Day")  # program ends when user inputs q for quit
else:
    print("No such item in Inventory")  # Program displays message if item type and manufacture is not in data
