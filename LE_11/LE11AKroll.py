# Name: Andrew Kroll
# Date: 2020-11-20
# Course-Section/LE#: CS1120-951 LE11
# Description: Stacks and queues


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        return item

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        for item in self.stack:
            print(item)

    def insert_at_bottom(self, item):
        self.stack.insert(0, item)

    def reverse_stack(self, stack):
        if not stack.is_empty():
            item = stack.pop()
            self.reverse_stack(stack)
            stack.insert_at_bottom(item)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            print("Queue is empty")
            return None
        return self.stack2.pop()


def main():

    # Stack Section #
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print("--- Displaying the stack contents ---")
    stack.display()
    stack.reverse_stack(stack)
    print("--- Displaying the reversed stack contents ---")
    stack.display()

    # Queue Section #
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    item = queue.dequeue()
    print("--- Displaying the queue contents ---")
    while item is not None:
        print(item)
        item = queue.dequeue()


main()
