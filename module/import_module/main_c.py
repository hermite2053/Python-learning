# import all of names except begin with '_' defined in the module
from sequences import *

print('triangular numbers:')
for x in range(11):
    print(triangular_number(x), end=' ')

print()

print('square pyramidal numbers:')
for x in range(11):
    print(square_pyramidal_number(x), end=' ')

print()

# module 'sequences' has not been imported.
# print(sequences.__name__)
