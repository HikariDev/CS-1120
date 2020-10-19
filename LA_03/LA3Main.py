def main():
    for i in range(1, 5):
        file_name = "sam_{}.txt".format(i)
        data = read_data_from_file(file_name)
        print("{}: {}".format(file_name, find_longest_path_length(data)))


def read_data_from_file(file_name):
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
    longest = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] != 'A':
                continue
            longest = max(longest,
                          find_max(find_path_length_recursive(data, [[False for xc in range(len(data[r]))] for xr in range(len(data))], r-1, c),
                                   find_path_length_recursive(data, [[False for xc in range(len(data[r]))] for xr in range(len(data))], r+1, c),
                                   find_path_length_recursive(data, [[False for xc in range(len(data[r]))] for xr in range(len(data))], r, c-1),
                                   find_path_length_recursive(data, [[False for xc in range(len(data[r]))] for xr in range(len(data))], r, c+1)))
    return longest


def find_path_length_recursive(data, checked, r, c):
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
    return max(max(a, b), max(c, d))


main()
