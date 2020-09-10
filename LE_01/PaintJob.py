# Name: Andrew Kroll
# Date: 2020-09-05
# Course-Section/LE#: CS1120-951 LE1
# Description: Calculates paint and labor requirements and costs to paint
#              a wall.

def main():
    sqft = float(input("Square feet of wall to be painted: "))
    paint_price_per_gallon = float(input("Cost of paint per gallon: $"))
    gallons_of_paint = sqft/112  # Calculates gallons of paint from sqft
    hours_of_labor = sqft/112*8  # Calculates hours of labor from sqft
    paint_cost = gallons_of_paint*paint_price_per_gallon  # Calculates paint
    # cost from gallons of paint and given paint price
    labor_cost = hours_of_labor*35  # Calculates cost of labor
    total_cost = paint_cost + labor_cost  # Calculates total cost
    print("Gallons of paint: {:,.2f}".format(gallons_of_paint))
    print("Hours of labor: {:,.2f}".format(hours_of_labor))
    print("Cost of paint: ${:,.2f}".format(paint_cost))
    print("Cost of labor: ${:,.2f}".format(labor_cost))
    print("Total cost: ${:,.2f}".format(total_cost))


main()
