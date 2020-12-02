# Name: Andrew Kroll
# Date: 2020-12-02
# Course-Section/PMT#: CS1120-951 PMT2
# Description: Programming Mastery Test Slot #2

class Customer:
    def __init__(self):
        self.credit_cards = []

    # Add credit card ‘card’ to list of cards
    def add_credit_card(self, card):
        self.credit_cards.append(card)

    # Return list of cards
    def get_credit_cards(self):
        return self.credit_cards

    # Calculate total cost of all cards for this customer and return total.
    def calculate_total_cashback(self):
        total = 0
        for card in self.credit_cards:
            total += card.get_cashback_amount()
        return total


class CreditCard:
    def __init__(self, description, online_exp, gas_exp, other_exp):
        self.description = description
        self.online_exp = online_exp
        self.gas_exp = gas_exp
        self.other_exp = other_exp

    # Return this credit card's description.
    def get_description(self):
        return self.description

    # Return the type of this card
    def get_type(self):
        return "Generic Card"

    # Calculate and return the cashback amount for this credit card.
    def get_cashback_amount(self):
        return 0


class Elite(CreditCard):
    def get_type(self):
        return "Elite Card"

    def get_cashback_amount(self):
        return self.online_exp * 0.10 + self.gas_exp * 0.05 + self.other_exp \
               * 0.02


class Classic(CreditCard):
    def get_type(self):
        return "Classic Card"

    def get_cashback_amount(self):
        return self.online_exp * 0.07 + self.gas_exp * 0.04 + self.other_exp \
               * 0.02


class VIP(CreditCard):
    def __init__(self, description, online_exp, other_exp):
        super().__init__(description, online_exp, 0, other_exp)

    def get_type(self):
        return "VIP Card"

    def get_cashback_amount(self):
        return self.online_exp * 0.05 + self.other_exp * 0.02


def main():
    cust = Customer()
    card1 = Elite("Convocation Luncheon", 100, 25, 150)   # (description, online_exp, gas_exp, other_exp)
    card2 = Classic("Faculty Supplies", 80, 40, 50)     # (description, online_exp, gas_exp, other_exp)
    card3 = VIP("Miscellaneous", 50, 100)   # (description, online_exp, other_exp)

    cust.add_credit_card(card1)
    cust.add_credit_card(card2)
    cust.add_credit_card(card3)

    cards = cust.get_credit_cards()

    print("List of Credit Card Expenses")
    print("============================\n")

    print(f'{"Card":<15}{"Description":<25}{"Cash-back"}')
    print(f'{"----":<15}{"-----------":<25}{"--------"}')

    for i in range(len(cards)):
        print(
            f'{cards[i].get_type():<15}{cards[i].get_description():<25}{"$"}'
            f'{cards[i].get_cashback_amount():>6,.2f}')

    print()
    print(
        f'{"Total cash-back: $"}{cust.calculate_total_cashback():>6,.2f}')

    card4 = Elite("Convocation Awards", 200, 0, 150)   # (description, online_exp, gas_exp, other_exp)
    card5 = Classic("Staff Appreciation", 250, 50, 150)   # (description, online_exp, gas_exp, other_exp)

    cust.add_credit_card(card4)
    cust.add_credit_card(card5)

    print()
    for i in range(len(cards)):
        print(
            f'{cards[i].get_type():<15}{cards[i].get_description():<25}{"$"}'
            f'{cards[i].get_cashback_amount():>6,.2f}')

    print()
    print(
        f'{"Total cash-back: $"}{cust.calculate_total_cashback():>6,.2f}')


main()
