class Ticket:
    def __init__(self):
        pass

    def get_name(self):
        pass

    def get_grade(self):
        pass

    def get_cost_of_ticket(self):
        pass

class Customer:
    def __init__(self):
        pass

    def get_name(self):
        pass

    def get_tickets(self):
        pass

    def add_ticket(self):
        pass

    def get_total_cost_of_tickets(self):
        pass

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
