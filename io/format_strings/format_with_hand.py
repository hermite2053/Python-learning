import math

for i in range(1, 11):
    print(repr(i).rjust(2), '\b! =', repr(math.factorial(i)).rjust(12))
