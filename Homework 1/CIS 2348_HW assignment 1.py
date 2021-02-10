# This program calculates the users birthday
print('Birthday Calculator')  # Title of program is displayed
print('Current Day')  # Prompts user to input current day
print('Month:')
C_Month = int(input())  # User inputs current month
print('Day:')
C_Day = int(input())  # User inputs current Day
print('Year:')
C_Year = int(input())  # User inputs current year
print('Birthday')  # Prompts user to input Birthday information
print('Month:')  # User inputs birth month
B_Month = int(input())
print('Day:')  # User inputs birth day
B_Day = int(input())
print('Year:')  # User inputs birth year
B_Year = int(input())
Dif_Year = C_Year - B_Year
print('You are', Dif_Year, 'Years old')
if C_Month == B_Month and C_Day == B_Day:
    print('Happy Birthday')
else:
    print('Goodbye')







