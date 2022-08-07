strings = ['dragon',
           'internationalization',
           'supersymmetry',
           'Python',
           'nightmare',
           'contribution',
           'mass']
n = 8

print('list:', strings)
print(n, 'letters or short words:')
for w in strings:
    if len(w) > n:
        continue
    print(w)
