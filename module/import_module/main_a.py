import sequences as seq
sq_py_num = seq.square_pyramidal_number


print('triangular numbers:')
for x in range(11):
    print(seq.triangular_number(x), end=' ')

print()

print('square pyramidal numbers:')
for x in range(11):
    print(sq_py_num(x), end=' ')

print()
