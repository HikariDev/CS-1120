# Name: Andrew Kroll
# Date: 2020-09-05
# Course-Section/LE#: CS1120-951 LE1
# Description: Calculates rainfall totals, and averages. Finds highest and
#              lowest rainfall months.

def main():
    data = []
    high = None
    low = None
    for i in range(12):  # Asks the user for rainfall data for each of 12
        # months
        data.append(float(input("Rainfall for month {} (in): ".format(i+1))))
        if low is None or data[i] < low[1]:  # Updates lowest month if lower
            # or not set
            low = [i, data[i]]
        if high is None or data[i] > high[1]:  # Updates highest month if
            # higher or not set
            high = [i, data[i]]
    total = sum(data)  # Gets the sum of all months
    average = total / len(data)  # Calculates the average rainfall
    print("Total rainfall: {:,.2f} in".format(total))
    print("Average rainfall: {:,.2f} in".format(average))
    print("Highest rainfall: Month {} had {:,.2f} in".format(high[0]+1,
                                                             high[1]))
    print("Lowest rainfall: Month {} had {:,.2f} in".format(low[0]+1, low[1]))


main()
