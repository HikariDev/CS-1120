# Name: Andrew Kroll
# Date: 2020-09-20
# Course-Section/LA#: CS1120-951 LA1
# Description: Generate and manipulate two two-dimensional arrays that are
#              sized based on validated user input.
# Note: The function names given in the LA1_F'20.docx file do not comply with
#       Python naming conventions and have been corrected for this application.

from LA_01 import ProcessList


def main():
    rows = get_rows()  # Get the number of rows from the user
    cols = get_cols(rows)  # Get the number of columns from the user

    process_list = ProcessList.ProcessList(rows, cols)  # Generate process_list
    # object
    process_list.randomly_fill_list()  # Fill the random numbers array with
    # random numbers
    process_list.compute_list_values()  # Compute values for computed values
    # array
    process_list.print_list()  # Display both the random and computed arrays


def get_rows() -> int:
    rows = 0
    while not 5 <= rows <= 20:  # Continue asking user for input until between
        # 5 and 20 (inclusive)
        try:
            rows = int(input("Enter number of rows in range [5, 20]: "))
            if not 5 <= rows <= 20:  # Alert user if outside range
                print("Invalid input.")
        except ValueError:  # Alert user if not an integer
            print("Input must be an integer.")
    return rows


def get_cols(rows: int) -> int:
    cols = 0
    while not 5 <= cols <= 20 or cols == rows:  # Continue asking user for
        # input until between 5 and 20 (inclusive), not equal to rows
        try:
            cols = int(input("Enter number of cols in range [5, 20], "
                             "except {}: ".format(rows)))
            if not 5 <= cols <= 20 or rows == cols:  # Alert user if outside
                # range
                print("Invalid input.")
        except ValueError:  # Alert user if not an integer
            print("Input must be an integer.")
    return cols


main()
