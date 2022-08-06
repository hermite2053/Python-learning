import math

n = 20
for i in range(2, n):
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            print(i, 'has a prime factor', j)
            break
    else:
        print(i, 'is a prime number')
