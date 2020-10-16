# Name: Andrew Kroll
# Date: 2020-10-16
# Course-Section/LE#: CS1120-951 LE4
# Description: Word List Writer: Write n words to file, n specified by user,
#   words specified by user.
# Word List Reader: Read words from file, find word count, longest word,
#   average word length, and duplicate words, then display data.
# High Score: Read high scores from a file. Display number of scores and
#   highest score with the name of who had that score.


def word_list_writer():
    count = int(input("How many words would you like to enter? "))
    with open("words.txt", 'w') as file:
        for i in range(count):
            file.write(input("Enter a word: "))
            file.write("\n")


def word_list_reader():
    word_count = 0
    longest_word = ""
    length_sum = 0
    duplicates = {}
    with open("words.txt", 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            if line == "":
                break
            word_count += 1
            if len(line) > len(longest_word):
                longest_word = line
            length_sum += len(line)
            if line.lower() in duplicates:
                duplicates[line.lower()] += 1
            else:
                duplicates[line.lower()] = 1
    length_avg = length_sum / word_count
    print("Words in File: {}\n"
          "Longest Word: {}\n"
          "Average Length: {}".format(word_count, longest_word, length_avg))
    for duplicate in duplicates:
        if duplicates[duplicate] > 1:
            print("'{}' was entered {} times".format(duplicate,
                                                     duplicates[duplicate]))


def high_score():
    record_count = 0
    highest_score = ["", 0]
    with open("scores.txt", 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            if line != "":
                record_count += 1
                name = line.split(",")[0]
                score = int(line.split(",")[1])
                if score > highest_score[1]:
                    highest_score = [name, score]
    print("Records: {}\n"
          "Highest Score: {}: {}".format(record_count, highest_score[0],
                                         highest_score[1]))


word_list_writer()
print()
word_list_reader()
print()
high_score()
