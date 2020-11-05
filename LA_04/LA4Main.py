# Name: Andrew Kroll
# Date: 2020-10-30
# Course-Section/LA#: CS1120-951 LA4
# Description: TODO: LATER
import re


class UserInterface:
    def __init__(self):
        self.file = ""
        self.translator = None
        self.text = ""

    # Calls the necessary methods to: display a greeting, ask the user what
    # s/he wants to do; update the
    # corpus file name and the text to be translated based on the user’s input,
    # uses these to initialize
    # a Translator object, and loops until the user no longer wants
    # to translate any sentences.
    def run_program(self):
        self.file = self.get_corpus_filename()
        self.text = self.get_source_text()
        self.translator = Translator(self.file, self.text)
        self.translate()

    # Displays the translation options to the user and, after reading
    # in the option selected by the user, sets
    # the name of the corpus file. Uses try-except to enforce correct input.
    def get_corpus_filename(self):
        print("What would you like to translate?:")
        print(" ( 1 ) English to French")
        print(" ( 2 ) French to English")
        selection = 0
        while not (selection == 1 or selection == 2):
            try:
                selection = int(input("Select an option: "))
            except ValueError:
                print("\n<Error> Invalid input! Input must be a number.\n")
            else:
                if not (selection == 1 or selection == 2):
                    print("\n<Error> Invalid input! Must be 1 or 2.\n")
        return "etf.csv" if selection == 1 else "fte.csv"

    # Requests the text the user wants to translate (i.e. the source text).
    def get_source_text(self):
        source = ""
        while len(source) == 0:
            source = input("What would you like to translate? ")
        return source

    # Uses the Translator object to translate the source text
    # and displays the translated text to the user.
    def translate(self):
        self.translator.read_corpus()
        self.translator.translate()


class Translator:
    def __init__(self, file: str, source: str):
        self.file = file
        self.source = source
        self.dict = {}
        pass

    # Reads in the data from the input file and stores the data in a two
    # dimensional list for easy retrieval during the translation process.
    def read_corpus(self):
        with open(self.file, 'r') as file:
            for line in file:
                line = line.strip()
                if "," in line:
                    self.dict[line.split(",")[0]] = line.split(",")[1]

    # Calls the necessary methods to perform the translation and
    # returns the translated text.
    def translate(self):
        out = ""
        capitalize_first = self.source[0] == self.source[0].upper()
        last_chars = re.sub("[a-zA-Z]", "",
                            self.source.split(" ")[
                                len(self.source.split(" "))-1])
        for word in self.source.split(" "):
            if len(out) > 0:
                out += " "
            out += self.__lookup(word)
        if capitalize_first:
            out = out.capitalize()
        out += last_chars
        print(" >> {}".format(out))

    # Accepts a word as parameter, looks up the word in the
    # appropriate corpus, and returns the corresponding
    # translation. If the word is not found in the
    # corpus, it returns the word received as parameter.
    def __lookup(self, word: str):
        temp = re.sub(r"[^a-zA-Z]", "", word).lower()
        if temp in self.dict:
            return self.dict[temp]
        return temp


# A method to display a greeting to the user should be included in your
# application:
# Displays a greeting to the user and indicates briefly what
# the program does.
def greeting():
    print("Welcome to the Translator! Bienvenue!!")
    print("You can translate sentences from English to French and vice "
          "versa!")
    pass


# Your project should also have a main method:
# Creates an instance of the UserInterface class,
# and uses that instance to run the program.
# You should handle the FileNotFoundError in main.
def main():
    greeting()
    flag = True
    while flag:
        ui = UserInterface()
        try:
            ui.run_program()
        except FileNotFoundError:
            print("\n<Error> Corpus file could not be found.\n")
        flag = True if input("Would you like to translate something else? "
                             "(y/n) ").lower().startswith("y") else False


main()
