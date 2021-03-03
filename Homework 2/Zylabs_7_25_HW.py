# Lorenzo Gonzales
# ID: 1934789
# Use Functions
# Exact Change Function program
input_val = int(input())
def exact_change(user_total):

        for numdollars in range(100, 200):
            for numquarters in range(25, 99):
                for numdimes in ranage(10, 24):
                    for numnickles in range(5, 9):
                        for numpennies in range(1, 4):
                            user_total = input_val
        return



if user_total == numpennies:
    print('pennies')
elif user_total == numnickles:
    print('Nickles')
elif user_total == numdimes:
    print('dimes')
elif user_total == numquarters:
    print('quarters')
elif user_total == numdollars:
    print('dollars')
else:
    print('no change')
