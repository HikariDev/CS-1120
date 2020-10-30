# Name: Andrew Kroll
# Date: 2020-10-30
# Course-Section/LA#: CS1120-951 LA4
# Description: TODO: LATER


class UserInterface:
    def __init__(self):
        pass
    # Calls the necessary methods to: display a greeting, ask the user what
    # s/he wants to do; update the
    # corpus file name and the text to be translated based on the user’s input,
    # uses these to initialize
    # a Translator object, and loops until the user no longer wants
    # to translate any sentences.

    def run_program(self):
        pass
    # Displays the translation options to the user and, after reading
    # in the option selected by the user, sets
    # the name of the corpus file. Uses try-except to enforce correct input.

    def get_corpus_filename(self):
        pass
    # Requests the text the user wants to translate (i.e. the source text).

    def get_source_text(self):
        pass
    # Uses the Translator object to translate the source text
    # and displays the translated text to the user.

    def translate(self):
        pass


class Translator:
    def __init__(self, file, input):
        pass
    # Reads in the data from the input file and stores the data in a two
    # dimensional list for easy retrieval during the translation process.

    def read_corpus(self):
        pass
    # Calls the necessary methods to perform the translation and
    # returns the translated text.

    def translate(self):
        pass
    # Uses the private method: “lookup(word)” to look up each English
    # word in the user’s input text, creates a string representing
    # the translation of the user’s input, and updates the corresponding
    # data attribute with the translation of the user’s text
    # (in French).

    def english_to_french(self):
        pass
    # Uses the private method: “lookup(word)” to look up each French
    # word in the user’s input text, creates a string representing the
    # translation of the user’s input, and updates the corresponding
    # data attribute with the translation of the user’s text (in English).

    def french_to_english(self):
        pass
    # Accepts a word as parameter, looks up the word in the
    # appropriate corpus, and returns the corresponding
    # translation. If the word is not found in the
    # corpus, it returns the word received as parameter.

    def __lookup(self, word):
        pass


# A method to display a greeting to the user should be included in your
# application:
# Displays a greeting to the user and indicates briefly what
# the program does.
def greeting():
    pass


# Your project should also have a main method:
# Creates an instance of the UserInterface class,
# and uses that instance to run the program.
# You should handle the FileNotFoundError in main.
def main():
    greeting()


main()
