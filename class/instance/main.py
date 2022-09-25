class Currency:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.user = []


    def add_user(self, user):
        self.user.append(user)


    def add_some_users(self, users):
        for user in users:
            self.user.append(user)


    def add_currency(self, x):
        self.value = self.value + x


    def print_currency(self):
        print(f'{self.value} {self.unit}')


    def print_user(self):
        print(self.user)


European_Union = ['Austria', 'Belgium', 'Cyprus', 'Estonia', 'Finland',
                'France', 'Germany', 'Greece', 'Ireland', 'Italy',
                'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
                'Portugal', 'Slovakia', 'Slovenia', 'Spain']

a = Currency(10, 'JPY')
b = Currency(20, 'EUR')

a.print_currency()
b.print_currency()

a.add_currency(100)
b.add_currency(10)

a.print_currency()
b.print_currency()

a.add_user('Japan')
b.add_some_users(European_Union)

a.print_user()
b.print_user()
