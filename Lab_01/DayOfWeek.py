# Name: Andrew Kroll
# Date: 2020-09-05
# Course-Section/LE#: CS1120-951 LE1
# Description: Converts number to day of week

def main():
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


main()
