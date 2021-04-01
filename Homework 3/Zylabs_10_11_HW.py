# Lorenzo Gonzales
# ID: 1934789
# Zylabs 10.11 CIS 2348 LAB: Nutritional Information (classes/constructors)
# TODO: Define constructor with parameters to initialize instance # attributes (name, fat, carbs, protein)
class FoodItem:
    # function has been initialized with name, fat, carbs and protein
    def __init__(self, name = 'none', fat = 0.00, carbs = 0.00, protein = 0.00): # code is initialized with name as a string, fats, carbs and protein as floats
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

# Default values are presented first
# Values for the first food item are presented second
first_selection = FoodItem()
first_selection.name = input()
first_selection.fat = float(input())
first_selection.carbs  = float(input())
first_selection.protein = float(input())
first_selection.num_servings = float(input()) # Connect to get_calories
print(FoodItem().print_info())  # default values of Food item class are printed
print('Number of calories for 1.00 serving(s): {:.2f}'.format(FoodItem.get_calories().num_servings))
print(first_selection.print_info()) # user inputted values are displayed
print('Number of calories for 1.00 serving(s): {:.2f}'.format(first_selection.get_calories().num_servings))