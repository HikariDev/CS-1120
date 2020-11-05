# Name: Andrew Kroll
# Date: 2020-10-30
# Course-Section/LA#: CS1120-951 LA4
# Description: Translate from English to French and French to English using
# parallel corpus
import re


class UserInterface:
    def __init__(self):
        """
        Initializes file, translator, and text variables.
        """
        self.file = ""
        self.translator = None
        self.text = ""

    def run_program(self):
        """
        Controls cycle of the program:
        Retrieves program mode from user.
        Retrieves text to be translated from user.
        Executes translation.
        """
        self.file = self.get_corpus_filename()
        self.text = self.get_source_text()
        self.translator = Translator(self.file, self.text)
        self.translate()

    def get_corpus_filename(self):
        """
        Prompts the user to enter which translation mode they would like to
        use.

        :return: The file name for the appropriate corpus file.
        """
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

    def get_source_text(self):
        """
        Prompts the user to enter the message they would like to translate.

        :return: The message to be translated.
        """
        source = ""
        while len(source) == 0:
            source = input("What would you like to translate? ")
        return source

    def translate(self):
        """
        Reads corpus file and executes translation in the Translator object.
        """
        self.translator.read_corpus()
        self.translator.translate()


class Translator:
    def __init__(self, file: str, source: str):
        """
        Initializes the file and source variables from arguments.
        Initializes an empty dict variable.

        :param file: The name of the corpus file.
        :param source: The source text to be translated.
        """
        self.file = file
        self.source = source
        self.dict = {}

    def read_corpus(self):
        """
        Reads the corpus file and enters it into the dict variable.
        """
        with open(self.file, 'r') as file:
            for line in file:
                line = line.strip()
                if "," in line:
                    self.dict[line.split(",")[0]] = line.split(",")[1]

    def translate(self):
        """
        Translates then displays the source message.
        """
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

    def __lookup(self, word: str):
        """
        Looks up a word in the dict, then returns the translated word or source
        word if no translation is present.

        :param word: The word to be translated.

        :return: The translated word, or source word if no translation is
        present.
        """
        temp = re.sub(r"[^a-zA-Z]", "", word).lower()
        if temp in self.dict:
            return self.dict[temp]
        return temp


def greeting():
    """
    Displays a greeting for the user.
    """
    print("Welcome to the Translator! Bienvenue!!")
    print("You can translate sentences from English to French and vice "
          "versa!")
    pass


def main():
    """
    Main program control. Loops translation until the user no longer wishes
    to translate anything else.
    """
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
