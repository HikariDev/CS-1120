# Name: Andrew Kroll
# Date: 2020-09-10
# Course-Section/LE#: CS1120-951 LE2
# Description: Prints a shrinking triangle of asterisks

def main():
    for i in range(5, 0, -1):
        for a in range(i):
            print("* ", end='')
        print()


main()
