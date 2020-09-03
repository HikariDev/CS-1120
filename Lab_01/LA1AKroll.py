# Name: Andrew Kroll
# Date: 2020-09-03
# Course-Section/LA#: CS1120-951 LA1
# Description: Converts number to day of week


def day_of_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]  # Array of days
    day_num = ""
    while not day_num.isnumeric() or (int(day_num) < 1 or int(day_num) > 7):
        # Will only exit loop if the user inputs a number between 1-7
        day_num = input("Enter the number 1-7: ")
        if day_num.isnumeric():  # Checks to make sure the user input a number
            if int(day_num) < 1 or int(day_num) > 7:  # Verifies within range
                print("{} is not between 1 and 7!".format(day_num))
        else:  # Warns the user if they didn't input a number
            print("{} is not a number between 1 and 7!".format(day_num))
    print("Day {} is {}".format(day_num, days[int(day_num)-1]))  # Prints the
    # day of the week, shifted by -1 to account for arrays starting at 0


def calories_from_fat(grams_of_fat: int) -> int:
    return grams_of_fat * 9


def calories_from_carbs(grams_of_carbs: int) -> int:
    return grams_of_carbs * 4


def nutrition():
    fat_grams = int(input("How many grams of fat? "))
    carb_grams = int(input("How many grams of carbs? "))

    print("{} calories from {}g of fat".format(calories_from_fat(fat_grams),
                                               fat_grams))
    print("{} calories from {}g of carbs".format(
        calories_from_carbs(carb_grams), carb_grams))


def paint_job():
    sqft = float(input("Square feet of wall to be painted: "))
    paint_price_per_gallon = float(input("Cost of paint per gallon: $"))
    gallons_of_paint = sqft/112
    hours_of_labor = sqft/112*8
    paint_cost = gallons_of_paint*paint_price_per_gallon
    labor_cost = hours_of_labor*35
    total_cost = paint_cost + labor_cost
    print("Gallons of paint: {:,.2f}".format(gallons_of_paint))
    print("Hours of labor: {:,.2f}".format(hours_of_labor))
    print("Cost of paint: ${:,.2f}".format(paint_cost))
    print("Cost of labor: ${:,.2f}".format(labor_cost))
    print("Total cost: ${:,.2f}".format(total_cost))


def rain():
    data = []
    high = None
    low = None
    for i in range(12):
        data.append(int(input("Rainfall for month {} (in): ".format(i+1))))
        if low is None or data[i] < low[1]:
            low = [i, data[i]]
        if high is None or data[i] > high[1]:
            high = [i, data[i]]
    total = sum(data)
    average = total / len(data)
    print("Total rainfall: {:,} in".format(total))
    print("Average rainfall: {:,.2f} in".format(average))
    print("Highest rainfall: Month {} @ {:,.2f} in".format(high[0]+1, high[1]))
    print("Lowest rainfall: Month {} @ {:,.2f} in".format(low[0]+1, low[1]))


day_of_week()
nutrition()
paint_job()
rain()
