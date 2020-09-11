import random
from pynput.keyboard import Key, Listener
from copy import copy


class Sudoku:
    def build(self):
        self.board = [[0] * 9 for i in range(9)]
        for x in range(9):
            for y in range(9):
                num = random.randint(1, 9)
                tries = 0
                while num in self.check(x, y) and tries < 50:
                    num = random.randint(1, 9)
                    tries += 1
                self.board[x][y] = num

    def check(self, x, y):
        numbers = []
        for nx in range(9):  # Check X line
            if not self.board[nx][y] in numbers:
                numbers.append(self.board[nx][y])
        for ny in range(9):  # Check Y Line
            if not self.board[x][ny] in numbers:
                numbers.append(self.board[x][ny])
        for nx in range((x//3)*3, ((x//3)+1)*3):  # Check Box X
            for ny in range((y//3)*3, ((y//3)+1)*3):  # Check Box Y
                if not self.board[nx][ny] in numbers:
                    numbers.append(self.board[nx][ny])
        return numbers

    def validate(self):
        numbers = []
        for x in range(9):
            numbers = []
            for y in range(9):
                if self.board[x][y] in numbers or self.board[x][y] == 0:
                    return False
                numbers.append(self.board[x][y])
        numbers = []
        for y in range(9):
            numbers = []
            for x in range(9):
                if self.board[x][y] in numbers or self.board[x][y] == 0:
                    return False
                numbers.append(self.board[x][y])
        numbers = []
        for nx in range((x//3)*3, ((x//3)+1)*3):  # Check Box X
            for ny in range((y//3)*3, ((y//3)+1)*3):  # Check Box Y
                if self.board[nx][ny] in numbers or self.board[x][y] == 0:
                    return False
                numbers.append(self.board[nx][ny])
        return True

    def display(self):
        print("\n"*10)
        conflicts = self.conflicts()
        for y in range(9):
            if y > 0 and y/3 == y//3:
                print("\u001b[37m---------|----------|---------")
            for x in range(9):
                if x > 0 and x/3 == x//3:
                    print("\u001b[37m| ", end='')
                form = " {} "
                if self.sel[0] == x and self.sel[1] == y:
                    form = "[{}]"
                if [x, y] in conflicts:  # Conflicting - Red
                    if self.perm_board[x][y] != 0:
                        form = "\u001b[35m" + form
                    else:
                        form = "\u001b[31m" + form
                elif self.board[x][y] == 0 and self.perm_board[x][y] == 0:
                    # Vacant - White
                    form = "\u001b[37m" + form
                elif self.perm_board[x][y] != 0:  # Fixed - Cyan
                    form = "\u001b[36m" + form
                else:  # Set - Green
                    form = "\u001b[32m" + form
                if self.board[x][y] == 0:
                    print(form.format("-"), end='')
                else:
                    print(form.format(self.board[x][y]), end='')
            print()
        print()

    def change(self, x, y, value):
        if self.perm_board[x][y] == 0:
            self.board[x][y] = value

    def _conflicts(self, x, y):
        data = []
        for nx in range(9):
            if self.board[nx][y] == self.board[x][y] and nx != x:
                if not [nx, y] in data and not self.board[nx][y] == 0:
                    data.append([nx, y])
        for ny in range(9):
            if self.board[x][ny] == self.board[x][y] and ny != y:
                if not [x, ny] in data and not self.board[x][ny] == 0:
                    data.append([x, ny])
        for nx in range((x//3)*3, ((x//3)+1)*3):  # Check Box X
            for ny in range((y//3)*3, ((y//3)+1)*3):  # Check Box Y
                if self.board[nx][ny] == self.board[x][y] and nx != x and \
                        ny != y:
                    if not [nx, ny] in data and not self.board[nx][ny] == 0:
                        data.append([nx, ny])
        if len(data) > 0:
            data.append([x, y])
        return data

    def conflicts(self):
        data = []
        for x in range(9):
            for y in range(9):
                for conflict in self._conflicts(x,y):
                    if not conflict in data:
                        data.append(conflict)
        return data

    print("Generating board. Please wait...")

    def main(self):
        self.board = []
        self.build()
        while not self.validate():
            self.build()
        print("Board generated!\n")
        # display(board)
        difficulty = int(input("What difficulty would you like? Easy (1), " +
                               "Medium (2), or Hard (3)? "))
        removed = 0
        while removed < difficulty*24:
            x = random.randint(0,8)
            y = random.randint(0,8)
            if self.board[x][y] != 0:
                self.board[x][y] = 0
                removed += 1
        self.perm_board = [[0]*9 for i in range(9)]
        for x in range(9):
            for y in range(9):
                self.perm_board[x][y] = int(self.board[x][y])
        self.sel = [0, 0]
        self.display()


sudoku = Sudoku()
sudoku.main()


def on_press(key):
    if key == Key.left:
        sudoku.sel[0] -= 1
    elif key == Key.right:
        sudoku.sel[0] += 1
    elif key == Key.up:
        sudoku.sel[1] -= 1
    elif key == Key.down:
        sudoku.sel[1] += 1
    if sudoku.sel[0] < 0:
        sudoku.sel[0] = 0
    elif sudoku.sel[0] > 8:
        sudoku.sel[0] = 8
    if sudoku.sel[1] < 0:
        sudoku.sel[1] = 0
    elif sudoku.sel[1] > 8:
        sudoku.sel[1] = 8
    try:
        if key.char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            sudoku.change(sudoku.sel[0], sudoku.sel[1], int(key.char))
        if key.char == 'q':
            raise SystemExit
    except SystemExit:
        print("\n\nGoodbye!")
        exit()
    except:
        pass
    sudoku.display()
    if sudoku.validate():
        print("\n\tYou win!")
        exit()


with Listener(on_press=on_press) as listener:
    listener.join()
