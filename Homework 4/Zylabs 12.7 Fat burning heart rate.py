# Lorenzo Gonzales
# ID: 1934789
# Zylabs HW 12.7 Fat-burning heart rate

def get_age():
    adults_age = int(input())  # user inputs persons age
    if adults_age <= 17 or adults_age >= 76:  # age range is set between 18 and 75
        raise ValueError('Invalid age.')  # The value error prints invalid age if not in range
    else:
        return adults_age

def fat_burning_heart_rate():
    heart_rate = (220 - adults_age) * 0.7  # 220 minus the persons age multiplied by 70 percent
    return heart_rate


if __name__ == "__main__":
    try:
        adults_age = get_age()  # get age function is connected
        heart_rate = fat_burning_heart_rate()  # heart rate function is connected
        print('Fat burning heart rate for a', adults_age, 'year-old:', heart_rate, 'bpm')
    except ValueError as exception:  # ValueError from get_age() connects to main
        print(exception)
        print('Could not calculate heart rate info.')
