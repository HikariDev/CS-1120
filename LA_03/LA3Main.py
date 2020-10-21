

def main():
    """
    Handles file selection, retrieval of longest path length, and display of
    longest path length.
    """
    for i in range(1, 5):
        file_name = "sam_{}.txt".format(i)
        data = read_data_from_file(file_name)
        print("{} Longest Path: {}".format(file_name,
                                           find_longest_path_length(data)))


def read_data_from_file(file_name):
    """
    Handles reading data from file into a two-dimensional array

    :param file_name: The name of the file to read from

    :return: A two-dimensional array of characters
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines[0] = lines[0].strip()
        width = int(lines[0].split(" ")[0])
        height = int(lines[0].split(" ")[1])
        data = [["" for c in range(width)] for r in range(height)]
        for r in range(1, len(lines)):
            line = lines[r].strip()
            for c in range(len(line)):
                data[r-1][c] = line[c]
        return data


def find_longest_path_length(data):
    """
    Iterates through all cells in the passed two-dimensional array and begins
    recursive search for the maximum path length

    :param data: A two-dimensional array of characters

    :return: The maximum path length in the two-dimensional array
    """
    longest = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] != 'A':
                continue
            checked = [[False for xc in range(len(data[r]))] for xr in
                       range(len(data))]
            checked[r][c] = True
            longest = max(longest, 1 +
                          find_max(find_path_length_recursive(data, checked,
                                                              r-1, c),
                                   find_path_length_recursive(data, checked,
                                                              r+1, c),
                                   find_path_length_recursive(data, checked,
                                                              r, c-1),
                                   find_path_length_recursive(data, checked,
                                                              r, c+1)))
    return longest


def find_path_length_recursive(data, checked, r, c):
    """
    Recursively search for the longest path in the two-dimensional array

    :param data: A two-dimensional character array

    :param checked: A two-dimensional boolean array

    :param r: The row number of the cell to check

    :param c: The column number of the cell to check

    :return: The maximum path length of neighboring cells, plus one
    """
    if r < 0 or c < 0 or r >= len(data) or c >= len(data[r]):
        return 0
    if data[r][c] != 'A' or checked[r][c] is True:
        return 0
    checked[r][c] = True
    return 1 + find_max(find_path_length_recursive(data, checked, r - 1, c),
                        find_path_length_recursive(data, checked, r + 1, c),
                        find_path_length_recursive(data, checked, r, c - 1),
                        find_path_length_recursive(data, checked, r, c + 1))


def find_max(a, b, c, d):
    """
    Finds the maximum value of four values

    :param a: A decimal number

    :param b: A decimal number

    :param c: A decimal number

    :param d: A decimal number

    :return: The largest number passed to the function
    """
    return max(max(a, b), max(c, d))


main()
