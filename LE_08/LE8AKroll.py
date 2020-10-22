# Name: Andrew Kroll
# Date: 2020-10-22
# Course-Section/LE#: CS1120-951 LE8
# Description:

import sys


def main():
    read_numbers()
    read_file()
    is_int(input("Enter a number: "))


def read_numbers():
    try:
        file = open("numbers.txt", 'r')
        total = 0
        count = 0
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) == 0:
                continue
            try:
                total += int(line)
                count += 1
            except ValueError:
                print("Error on line {} in file numbers.txt: Expected number "
                      "but got '{}'".format(i, line))
        print("Average value in file: {}".format(total/count))
        file.close()
    except IOError:
        print("Error: File 'numbers.txt' could not be found!")


def read_file():
    if len(sys.argv) < 2:
        print("No target file specified."
              "Usage: 'Python3 LE8AKroll.py (File Name)'")
        return
    file_name = sys.argv[1]
    try:
        file = open(file_name, 'r')
        for line in file:
            print(line.strip())
        file.close()
    except IOError:
        print("Error: File '{}' could not be found!".format(file_name))


def is_int(arg):
    try:
        int(arg)
        print("{} is a number".format(arg))
    except ValueError:
        print("{} is not a number".format(arg))


main()
