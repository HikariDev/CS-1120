# Name: Andrew Kroll
# Date: 2020-11-13
# Course-Section/LE#: CS1120-951 LE10
# Description: Postfix Expression Evaluator


def evaluate(exp):
    stack = []
    parts = exp.split(",")
    for part in parts:
        try:
            if part == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif part == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif part == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif part == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(a/b)
            else:
                stack.append(int(part))
        except IndexError:
            print("Invalid expression. Please check to make sure there are no"
                  "missing numbers or operators! '{}'".format(exp))
            return 0
        except ValueError:
            print("Invalid character encountered in {}. Only +-*/ or "
                  "numbers are permitted.".format(exp))
            return 0
    return stack.pop()


def main():
    while True:
        exp = input("Enter a postfix arithmetic expression: ")
        print(exp, "=", evaluate(exp))
        print()
        if input("Would you like to evaluate another expression? "
                 "(y/n) ").lower() != "y":
            break
        print()


main()
