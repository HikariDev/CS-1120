from datetime import datetime
from datetime import timedelta


class LibraryItem:
    def __init__(self, call_num):
        """
        Initializes the LibraryItem object. Updates call_num, checked_out,
        date_checked_out, and due_date with provided or default values.

        :param call_num: the LibraryItem's call number.
        """
        self.call_num = call_num
        self.checked_out = False
        self.date_checked_out = "0000-00-00"
        self.due_date = "0000-00-00"

    def check_out(self):
        """
        Marks the LibraryItem as checked out and updates the date_checked_out
        to today.
        """
        self.checked_out = True
        self.date_checked_out = datetime.date(datetime.now())

    def get_call_number(self) -> str:
        """
        Returns the LibraryItem's call number.

        :return: the LibraryItem's call number.
        """
        return self.call_num

    def is_checked_out(self) -> bool:
        """
        Returns whether the LibraryItem is checked out or not.

        :return: the boolean value of checked_out.
        """
        return self.checked_out

    def get_date_checked_out(self) -> str:
        """
        Returns when the LibraryItem was checked out.

        :return: the date_checked_out string.
        """
        return self.date_checked_out

    def get_due_date(self) -> str:
        """
        Returns the LibraryItem's due date.

        :return: the due_date string.
        """
        return self.due_date

    def set_due_date(self, due_date: str):
        """
        Updates the LibraryItem's due date.

        :param due_date: the new due date string.
        """
        self.due_date = due_date

    def __str__(self) -> str:
        """
        Returns information about the LibraryItem's call number and checkout
        status.

        :return: a formatted string of the call number, checked out status,
        date out, and due date (if checked out).
        """
        if self.checked_out:
            return "Call Number: {}\n" \
                   "Checked Out: YES\n" \
                   "Date Out: {}\n" \
                   "Date Due: {}".format(self.call_num, self.date_checked_out,
                                         self.due_date)
        return "Call Number: {}\n" \
               "Checked Out: NO".format(self.call_num)


class Book(LibraryItem):
    def __init__(self, call_num: str, title: str, author: str, genre: str):
        """
        Initializes the Book object with provided call number, title, author,
        and genre values.

        :param call_num: the book's call number.
        :param title: the book's title.
        :param author: the book's author.
        :param genre: the book's genre.
        """
        super().__init__(call_num)
        self.title = title
        self.author = author
        self.genre = genre

    def check_out(self):
        """
        Marks the book as checked out and updates the due date to 21 days
        from now.
        """
        super().check_out()
        self.set_due_date(str(datetime.date(datetime.now()
                                            + timedelta(days=21))))

    def __str__(self) -> str:
        """
        Returns information about the book's title, author, genre, and
        checked out status.

        :return: a formatted string of the title, author, genre, call number,
        checked out status, and the date out and due date if checked out.
        """
        return "\n" \
               "Book Title: {}\n" \
               "Author: {}\n" \
               "Genre: {}\n" \
               "{}".format(self.title, self.author, self.genre,
                           super().__str__())


class Periodical(LibraryItem):
    def __init__(self, call_num: str, title: str, volume: int, issue: int,
                 subject: str):
        """
        Initializes the Periodical object with the provided call number,
        title, volume number, issue number, and subject.

        :param call_num: the periodical's call number.
        :param title: the periodical's title.
        :param volume: the periodical's volume number.
        :param issue: the periodical's issue number.
        :param subject: the periodical's subject.
        """
        super().__init__(call_num)
        self.title = title
        self.volume = volume
        self.issue = issue
        self.subject = subject

    def check_out(self):
        """
        Marks the book as checked out and updates the due date to 7 days
        from now.
        """
        super().check_out()
        self.set_due_date(str(datetime.date(datetime.now()
                                            + timedelta(days=7))))

    def __str__(self) -> str:
        """
        Returns information about the periodical's title, volume and issue
        numbers, subject, and checked out status.

        :return: a formatted string of title, volume and issue numbers,
        subject, checked out status, and the date out and due date if
        checked out.
        """
        return "\n" \
               "Periodical Title: {}\n" \
               "Volume: {}\n" \
               "Issue: {}\n" \
               "Subject: {}\n" \
               "{}".format(self.title, self.volume, self.issue, self.subject,
                           super().__str__())


class Controller:
    def __init__(self):
        """
        Initializes the Controller object with empty books and periodicals
        dictionaries.
        """
        self.books = {}
        self.periodicals = {}

    def show_menu(self):
        """
        Displays the Library Catalog System menu.
        """
        print()
        print("--------- Menu ---------")
        print(" 1) Display Collection")
        print(" 2) Check out materials")
        print(" 3) Quit")
        print("------------------------")

    def display_collection(self):
        """
        Displays each registered book and periodical.
        """
        for book in self.books:  # Display each book
            print(self.books[book])
        for periodical in self.periodicals:  # Display each periodical
            print(self.periodicals[periodical])

    def find_item(self, call_num: str) -> LibraryItem:
        """
        Returns the requested book or periodical if registered.

        :param call_num: the book or periodical's call number.
        :return: the book or periodical object if registered, otherwise None.
        """
        call_num = call_num.upper()
        if call_num in self.books:  # Check in books
            return self.books[call_num]
        if call_num in self.periodicals:  # Check in periodicals
            return self.periodicals[call_num]

    def check_out_materials(self):
        """
        Asks the user which item they want to check out. Alerts user if
        item is unavailable. Checks out item if available.
        """
        call_num = input("\nEnter the call number: ").upper()
        item = self.find_item(call_num)
        if item is None or item.is_checked_out():  # Not registered or already
            # checked out
            print("Item is not available.")
        else:  # Available
            item.check_out()
            print(str(item))

    def read_input(self, file_name: str):
        """
        Reads all library item information from the targeted file.

        :param file_name: the name of the library item information file.
        """
        with open(file_name, 'r') as file:  # Opens the specified file to read
            for line in file:
                line = line.rstrip("\n")  # Removes trailing newline
                lines = line.split(",")  # Splits line to be passed
                if line.startswith("P"):  # Periodical
                    self.periodicals[lines[1].upper()] = \
                        Periodical(lines[1], lines[2], int(lines[3]),
                                   int(lines[4]), lines[5])
                elif line.startswith("B"):  # Book
                    self.books[lines[1].upper()] = \
                        Book(lines[1], lines[2], lines[3], lines[4])


def main():
    """
    The main method. Controls the main application loop.
    """
    control = Controller()  # Creates a Controller object
    control.read_input("input.txt")  # Reads the input.txt file
    response = ""
    quit_flag = False  # Tells the loop whether to continue or to stop
    while quit_flag is False:  # Infinitely loops until told to stop
        control.show_menu()  # Displays the program menu
        response = input("Please choose an option: ")
        if response == "1":  # Display Collection
            control.display_collection()
        elif response == "2":  # Checkout Item
            control.check_out_materials()
        elif response == "3":  # Quit
            quit_flag = True
        else:  # Invalid
            print("Invalid Response!")
    print("Goodbye!")


main()
