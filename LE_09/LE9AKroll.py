# Name: Andrew Kroll
# Date: 2020-11-06
# Course-Section/LE#: CS1120-951 LE9
# Description: magic_8_ball: Displays one of 12 random messages in response
#   to a question.
# prime_number_generator: Generates and displays a list of all prime numbers
#   less than or equal to the number the user enters.

import random


def magic_8_ball():
    responses = []
    with open("8_ball_responses.txt", 'r') as file:
        for line in file:
            line = line.strip()
            responses.append(line)
    run = True
    print("-- Magic 8-Ball --")
    while run:
        input("\nWhat's your question? ")
        print("> Magic 8-Ball: {}".format(responses[
                                              random.randint(0,
                                                             len(responses))]))
        if not input("\nWould you like to play again? (y/n) ").lower() == "y":
            run = False


def prime_number_generator():
    print("-- Prime Number Generator --")
    num = 0
    while num <= 1:
        try:
            num = int(input("\nEnter an integer greater than 1: "))
        except ValueError:
            print("Error: you must input an integer.")
            num = 0
        else:
            if num <= 1:
                print("Error: you must input an integer greater than 1.")
    nums = []
    for i in range(2, num+1):
        nums.append(i)
    print("Prime numbers less than or equal to {}:".format(num))
    for num in nums:
        if is_prime(num):
            print(" > {}".format(num))


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


magic_8_ball()
prime_number_generator()