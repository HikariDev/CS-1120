from datetime import datetime
from datetime import timedelta


class LibraryItem:
    # Initializes the LibraryItem object with the provided call number.
    # Defines checked_out as False, date_checked_out and due_date as 0000-00-00
    # @parameter call_num - the item's call number
    def __init__(self, call_num):
        self.call_num = call_num
        self.checked_out = False
        self.date_checked_out = "0000-00-00"
        self.due_date = "0000-00-00"

    # Marks the item as checked out and updates the date_checked_out to today.
    def check_out(self):
        self.checked_out = True
        self.date_checked_out = datetime.date(datetime.now())

    # Returns the item's call number
    # @return - a call number string
    def get_call_number(self) -> str:
        return self.call_num

    # Returns if the item is checked out
    # @return - boolean value for checked_out
    def is_checked_out(self) -> bool:
        return self.checked_out

    # Returns the date checked out
    # @return - date checked out string
    def get_date_checked_out(self) -> str:
        return self.date_checked_out

    # Returns the currently set due date
    # @return - a due date string
    def get_due_date(self) -> str:
        return self.due_date

    # Sets the due date to the provided value
    # @parameter due_date - the item's new due date
    def set_due_date(self, due_date: str):
        self.due_date = due_date

    # Returns information about this LibraryItem's call number, checked out
    # status, date out, and due date.
    # @return - information about the LibraryItem.
    def __str__(self) -> str:
        if self.checked_out:
            return "Call Number: {}\n" \
                   "Checked Out: YES\n" \
                   "Date Out: {}\n" \
                   "Date Due: {}".format(self.call_num, self.date_checked_out,
                                         self.due_date)
        return "Call Number: {}\n" \
               "Checked Out: NO".format(self.call_num)


class Book(LibraryItem):
    # Initializes the Book object with the given call number, title, author,
    # and genre. Calls the parent LibraryItem class initializer.
    # @parameter call_num - the book's call number
    # @parameter title - the book's title
    # @parameter author - the book's author
    # @parameter genre - the book's genre
    def __init__(self, call_num, title, author, genre):
        super().__init__(call_num)
        self.title = title
        self.author = author
        self.genre = genre

    # Checks out the item and updates the due date.
    def check_out(self):
        super().check_out()
        self.set_due_date(str(datetime.date(datetime.now()
                                            + timedelta(days=21))))

    # Returns information about this book's title, author, genre, and check out
    # status.
    # @return - information about the book.
    def __str__(self) -> str:
        return "\n" \
               "Book Title: {}\n" \
               "Author: {}\n" \
               "Genre: {}\n" \
               "{}".format(self.title, self.author, self.genre,
                           super().__str__())


class Periodical(LibraryItem):
    # Initializes the Periodical object with the given call number, title,
    # volume, issue, and subject. Calls parent LibraryItem class initializer.
    # @parameter call_num - the periodical's call number
    # @parameter title - the periodical's title
    # @parameter volume - the periodical's volume number
    # @parameter issue - the periodical's issue number
    # @parameter subject - the periodical's subject
    def __init__(self, call_num, title, volume, issue, subject):
        super().__init__(call_num)
        self.title = title
        self.volume = volume
        self.issue = issue
        self.subject = subject

    # Checks out the item and updates the due date.
    def check_out(self):
        super().check_out()
        self.set_due_date(str(datetime.date(datetime.now()
                                            + timedelta(days=7))))

    # Returns information about this periodical's title, volume, issue,
    # subject, and check out status.
    # @return - information about the periodical.
    def __str__(self) -> str:
        return "\n" \
               "Periodical Title: {}\n" \
               "Volume: {}\n" \
               "Issue: {}\n" \
               "Subject: {}\n" \
               "{}".format(self.title, self.volume, self.issue, self.subject,
                           super().__str__())


class Controller:
    # Initializes the Controller object with empty books and periodicals
    # dictionaries
    def __init__(self):
        self.books = {}
        self.periodicals = {}

    # Displays the navigation menu text
    def show_menu(self):
        print()
        print("--------- Menu ---------")
        print(" 1) Display Collection")
        print(" 2) Check out materials")
        print(" 3) Quit")
        print("------------------------")

    # Displays each registered book and periodical
    def display_collection(self):
        for book in self.books:  # Display each book
            print(self.books[book])
        for periodical in self.periodicals:  # Display each periodical
            print(self.periodicals[periodical])

    # Returns the desired library item if registered.
    # @return - a LibraryItem object or None
    # @parameter call_num - the desired item's call number
    def find_item(self, call_num: str) -> LibraryItem:
        call_num = call_num.upper()
        if call_num in self.books:  # Check in books
            return self.books[call_num]
        if call_num in self.periodicals:  # Check in periodicals
            return self.periodicals[call_num]

    # Asks the user which item they would like to check out.
    # Checks out the item if available.
    # Alerts user if item is not registered or already checked out.
    def check_out_materials(self):
        call_num = input("\nEnter the call number: ").upper()
        item = self.find_item(call_num)
        if item is None or item.is_checked_out():  # Not registered or already
            # checked out
            print("Item is not available.")
        else:  # Available
            item.check_out()
            print(str(item))

    # Reads input from the specified library item file.
    # @parameter file_name - the targeted library data file's name
    def read_input(self, file_name):
        with open(file_name, 'r') as file:  # Opens the specified file to read
            for line in file:
                line = line.rstrip("\n")  # Removes trailing newline
                lines = line.split(",")  # Splits line to be passed
                if line.startswith("P"):  # Periodical
                    self.periodicals[lines[1].upper()] = \
                        Periodical(lines[1], lines[2], lines[3], lines[4],
                                   lines[5])
                elif line.startswith("B"):  # Book
                    self.books[lines[1].upper()] = \
                        Book(lines[1], lines[2], lines[3], lines[4])


def main():
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
