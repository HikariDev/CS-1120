# Name: Andrew Kroll
# Date: 2020-09-20
# Course-Section/LA#: CS1120-951 LA1
# Description: Handle data processing for array manipulation.

import random


class ProcessList:

    def __init__(self, rows: int, cols: int):  # Initializes the ProcessList
        # object
        self.rows = rows  # Defines the number of rows
        self.cols = cols  # Defines the number of columns
        self.random_numbers = [[0 for col in range(cols)]
                               for row in range(rows)]  # Define random_numbers
        # variable as a two dimensional array of 0's with rows rows and cols
        # cols
        self.computed_numbers = [[0 for col in range(cols)]
                                 for row in range(rows)]  # Define
        # computed_numbers variable as a two dimensional array of 0's with rows
        # rows and cols cols

    def randomly_fill_list(self):  # Fills the random_numbers array with
        # randomly generated numbers between 0 and 15
        for row in range(self.get_rows()):  # Iterate through row values
            for col in range(self.get_rows()):  # Iterate through col values
                self.set_random_number(row, col, random.randint(0, 15))
                # Set the cell to a random number between 0 and 15 (inclusive)

    def compute_list_values(self):  # Fills the computed_numbers array with
        # the sum of all neighboring cells from random_numbers array
        for row in range(self.get_rows()):  # Iterate through row values
            for col in range(self.get_rows()):  # Iterate through col values
                neighbor_sum = 0  # Used to temporarily hold the sum of all
                # neighboring cells
                for n_row in range(max(0, row-1), min(self.get_rows(), row+2)):
                    # Iterate through neighboring rows
                    for n_col in range(max(0, col-1), min(self.get_rows(),
                                                          col+2)):
                        # Iterate through neighboring cols
                        if n_row != row or n_col != col:
                            # Prevent adding current cell to neighbor cell sum
                            neighbor_sum += self.get_random_number(n_row,
                                                                   n_col)
                self.set_computed_number(row, col, neighbor_sum)
                # Set computed cell value

    def print_list(self):  # Displays both the random_numbers and
        # computed_numbers arrays with appropriate padding.
        print("Initial list with random numbers:")
        for row in range(self.rows):  # Iterate through row values
            for col in range(self.cols):  # Iterate through col values
                print(" {:>3n}".format(self.get_random_number(row, col)),
                      end='')  # Print cell aligned to right with 3 digit
                # padding
            print()  # Ends the current row's line
        print("Computed list:")
        for row in range(self.rows):  # Iterate through row values
            for col in range(self.cols):  # Iterate through col values
                print(" {:>3n}".format(self.get_computed_number(row, col)),
                      end='')  # Print cell aligned to right with 3 digit
                # padding
            print()  # Ends the current row's line

    def get_rows(self) -> int:  # Gets the set number of rows
        return self.rows

    def get_cols(self) -> int:  # Gets the set number of cols
        return self.cols

    def get_random_number(self, row: int, col: int) -> int:
        # Gets the targeted cell value from random_numbers array
        return self.random_numbers[row][col]

    def set_random_number(self, row: int, col: int, val: int):
        # Sets the targeted cell value in random_numbers array
        self.random_numbers[row][col] = val

    def get_computed_number(self, row: int, col: int) -> int:
        # Gets the targeted cell value from computed_numbers array
        return self.computed_numbers[row][col]

    def set_computed_number(self, row: int, col: int, val: int):
        # Sets the targeted cell value in computed_numbers array
        self.computed_numbers[row][col] = val
