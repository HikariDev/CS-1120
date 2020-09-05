# Name: Andrew Kroll
# Date: 2020-09-05
# Course-Section/LE#: CS1120-951 LE1
# Description: Calculates calories from grams of fat and carbs.

def main():
    fat_grams = int(input("How many grams of fat? "))
    carb_grams = int(input("How many grams of carbs? "))

    fat_calories = fat_grams * 9  # Calculates number of calories from fat
    # grams
    carb_calories = carb_grams * 4  # Calculates number of calories from carb
    # grams

    print("{} calories from {}g of fat".format(fat_calories, fat_grams))
    print("{} calories from {}g of carbs".format(carb_calories, carb_grams))


main()
