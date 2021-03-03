# Lorenzo Gonzales
# ID:1934789
# Brute Force Equation solver
# x + y = z program solves Linear Equations
x_val = int(input())
y_val = int(input())
z_val = int(input())
x_vale = int(input())
y_vale = int(input())
z_vale = int(input())
while x in range(-10, 10):  # values of x are set between -10 and 10
    while y in range(-10, 10):  # values of y are set between -10 and 10
        if x_val * x + y_val * y == z_val and x_vale * x + y_vale * y == z_vale:
            print(x, y)  # values of x, y are printed
else:
    print('No solution')  # if the range is off then no solution is printed
