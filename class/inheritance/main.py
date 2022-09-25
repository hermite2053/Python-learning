class two_num:
    def __init__(self, i1, i2):
        self.i1 = i1
        self.i2 = i2


    def sum(self):
        return self.i1 + self.i2


    def print_elm1(self):
        print(self.i1)


    def print_elm2(self):
        print(self.i2)


class three_num(two_num):
    def __init__(self, i1, i2, i3):
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3


    # override
    def sum(self):
        return self.i1 + self.i2 + self.i3


    def print_elm3(self):
        print(self.i3)


a = two_num(2, 3)
print(a.sum())
a.print_elm1()
a.print_elm2()

b = three_num(10, 20, 30)
print(b.sum())
b.print_elm1()
b.print_elm2()
b.print_elm3()
