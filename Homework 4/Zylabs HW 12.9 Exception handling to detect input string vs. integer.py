# Lorenzo Gonzales
# ID: 1934789
# Zylabs HW 12.9 Exception handling to detect input string vs. integer
parts = input().split()
name = parts[0]
age = parts[1]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except:
        print('{} {}'.format(name, age))
        name = (parts[0]) + 1
        age = 0

    parts = input().split()
    name = parts[0]
