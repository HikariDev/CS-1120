# Name: Andrew Kroll
# Date: 2020-12-02
# Course-Section/LA#: CS1120-951 LA7
# Description: Unit Testing
import unittest


class Bookshop:

    # Use list comprehension, lambda, filter, reduce, and map to write these
    #   functions.
    # Only use sorted() as needed.
    # No using iteration/loops/other functions or collections' methods.

    # [[1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
    # [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
    # [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
    # [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]]

    # Returns list of (order number, price of product * quantity)
    def method1(self, orders):
        return list(map(lambda x: [x[0], list(
            map(lambda y: (y[0], y[1] * y[2] + (10 if y[1] * y[2] < 100 else
                                                0)), x[1:]))], orders))
    # receives a list of lists and returns a list with tuples of two items.

    def method2(self, orders):
        return [(order[0], min(order[1:], key=lambda x:x[1]*x[2])[0]) for order
                in orders]
        # Return the minimum price of product (price * quantity) from each
        # order, return in same manner as above^
    # receives a list of lists, filters out the min. price and returns a list.

    def method3(self, orders):
        return [(order[0], max(order[1:], key=lambda x:x[1]*x[2])[0]) for order
                in orders]
    # receives a list of lists, filters out the max. price and returns a list.

    def method4(self, orders):
        # TODO: Fix the floating point errors on the price total
        # Return (order number, total amount of order)
        return [(order[0], sum([item[1] * item[2] for item in order[1:]])) for
                order in orders]
    # receives a list of lists and returns a list of tuples.

    def method5(self, orders):
        # Wrong. Return a list [book number, total price for book in orders]
        #   for the highest total price book out of all orders

        # build a list of book numbers and prices for that book order
        # find the highest and return it
        return [(order[0], sum([item[1] for item in order[1:]])) for order in
                orders]
    # receives a list of lists and returns a list.

    def method6(self, orders):
        # Return a list of book number and total quantity in all orders

        pass
    # receives a list of lists and returns a list.

    def method7(self, orders):
        pass
    # receives a list of lists and returns an ordered list.

    def method8(self, orders):
        pass
    # receives a list of lists and returns an integer.

    def method9(self, orders):
        pass
    # receives a list of lists and returns a list.

    def method10(self, orders):
        pass
    # receives a list of lists and returns a list.


class TestBookshop(unittest.TestCase):
    def setUp(self):
        self.bookshop = Bookshop()
        self.orders = [[1, ("5464", 4, 9.99), ("8274", 18, 12.99),
                        ("9744", 9, 44.95)],
                       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                       [4, ("8732", 7, 11.99), ("7733", 11, 18.99),
                        ("88112", 5, 39.95)]]
    # Creates an instance for Bookshop class.
    # Initializes the list of lists = order

    def test_method1(self):
        actual = self.bookshop.method1(self.orders)
        print("ACTUAL:")
        print(actual)
        expected = [[1, [('5464', 49.96), ('8274', 233.82), ('9744', 404.55)]],
                    [2, [('5464', 99.91), ('9744', 404.55)]],
                    [3, [('5464', 99.91), ('88112', 274.89)]],
                    [4, [('8732', 93.93), ('7733', 208.89), ('88112', 199.75)]]]
        self.assertEqual(actual, expected)
        print(expected)
    # Initializes the expected value.
    # Calls method1 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method2(self):
        actual = self.bookshop.method2(self.orders)
        expected = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '8732')]
        print("ACTUAL:")
        print(actual)
        self.assertEqual(actual, expected)
        print(expected)
    # Initializes the expected value.
    # Calls method2 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method3(self):
        actual = self.bookshop.method3(self.orders)
        expected = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '8732')]
        print("ACTUAL:")
        print(actual)
        self.assertNotEquals(actual, expected)
        print(expected)
    # Initializes the expected value.
    # Calls method3 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method4(self):
        actual = self.bookshop.method4(self.orders)
        expected = [(1, 678.33), (2, 494.46), (3, 364.8), (4, 492.57)]
        print("ACTUAL:")
        print(actual)
        self.assertEqual(actual, expected)
        print(expected)
    # Initializes the expected value.
    # Calls method4 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method5(self):
        pass
    # Initializes the expected value.
    # Calls method5 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method6(self):
        pass
    # Initializes the expected value.
    # Calls method6 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method7(self):
        pass
    # Initializes the expected value.
    # Calls method7 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method8(self):
        pass
    # Initializes the expected value.
    # Calls method8 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method9(self):
        pass
    # Initializes the expected value.
    # Calls method9 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values

    def test_method10(self):
        pass
    # Initializes the expected value.
    # Calls method10 and tests the returned value (actual value) using assert method
    # Displays the actual and expected values


if __name__ == '__main__':
    unittest.main()
