class Ticket:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def get_cost_of_ticket(self):
        return 0


class Exclusive(Ticket):
    def __init__(self, name, grade):
        super().__init__(name, grade)

    def get_cost_of_ticket(self):
        if self.get_grade() == 'f':
            return 10000 + 3000
        elif self.get_grade() == 'c':
            return 10000 + 2000
        return 10000


class PremiumPlus(Ticket):
    def __init__(self, name, grade):
        super().__init__(name, grade)

    def get_cost_of_ticket(self):
        if self.get_grade() == 'f':
            return 6000 + 3500
        elif self.get_grade() == 'c':
            return 6000 + 2500
        return 6000


class EconomyComfort(Ticket):
    def __init__(self, name, grade, passengers):
        super().__init__(name, grade)
        self.passengers = passengers

    def get_cost_of_ticket(self):
        return 1200 * self.passengers


class Customer:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def get_name(self):
        return self.name

    def get_tickets(self):
        return self.tickets

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_total_cost_of_tickets(self):
        cost = 0
        for ticket in self.get_tickets():
            cost += ticket.get_cost_of_ticket()
        return cost


def main():
    jeweler = Customer("Maggie May")
    cust1 = Exclusive("John Smith", 'f')
    cust2 = PremiumPlus("Jane Jones", 's')
    cust3 = EconomyComfort("Ruth Sharp", 'c', 2)

    jeweler.add_ticket(cust1)
    jeweler.add_ticket(cust2)
    jeweler.add_ticket(cust3)

    print("Maggie's Jewerls List of Passengers")
    print("===================================\n")
    print("NOTE: 'c' -> couple; 'f' -> family; 's' -> single\n")

    tickets = jeweler.get_tickets()
    for ticket in tickets:
        print(f'{ticket.get_name():<17}{"("}{str(ticket.get_grade())}{")"}'
              f'{"   $"}{ticket.get_cost_of_ticket():>10,.2f}')
    print()
    print(f'{"Total cost of tickets: $"}'
          f'{jeweler.get_total_cost_of_tickets():>10,.2f}')

    cust4 = Exclusive("Dempsy Dean", 'c')
    cust5 = EconomyComfort("Sophia Weather", 'f', 5)

    jeweler.add_ticket(cust4)
    jeweler.add_ticket(cust5)

    print()
    for ticket in tickets:
        print(f'{ticket.get_name():<17}{"("}{str(ticket.get_grade())}{")"}'
              f'{"   $"}{ticket.get_cost_of_ticket():>10,.2f}')
    print()
    print(f'{"Total cost of tickets: $"}'
          f'{jeweler.get_total_cost_of_tickets():>10,.2f}')


main()
