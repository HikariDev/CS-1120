# Name: Andrew Kroll
# Date: 2020-10-01
# Course-Section/LA#: CS1120-951 LE5
# Description: Create several functions to perform different tasks...
#   largest_list_item: Accepts a list as an argument and returns the largest
#       value in the list using recursion.
#   sum_of_numbers: Accepts an integer argument and returns the sum of all
#       numbers from 1 to n using recursion.
#   recursive_power: Accepts a number to be raised, and an exponent as
#       arguments, then calculates the exponent using recursion.
#   palindrome: Accepts a word as an argument and checks if it's a palindrome.

def largest_list_item(lst, size):
    if size == 1:
        return lst[0]
    return max(lst[size-1], largest_list_item(lst, size-1))


def sum_of_numbers(start: int, end: int):
    if start == end:
        return start
    return sum_of_numbers(start, end-1) + end


def recursive_power(num: int, power: int):
    if power <= 0:
        return 1
    return num * recursive_power(num, power-1)
 

def palindrome(txt: str):
    txt = txt.lower()
    low = 0
    high = len(txt)-1
    while low < high:
        if txt[low] != txt[high]:
            return False
        low += 1
        high -= 1
    return True
