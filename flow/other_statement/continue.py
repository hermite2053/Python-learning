strings = ['dragon',
           'internationalization',
           'supersymmetry',
           'Python',
           'nightmare',
           'contribution',
           'mass']
n = 10

print('list:', strings)
print('10 letters or short words:')
for w in strings:
    if len(w) > 10:
        continue
    print(w)
