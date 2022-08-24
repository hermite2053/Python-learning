# if statements can be nested.
x = int(input('enter any integer: '))

if x > 3:
    if x < 8:
        print(x, '> 3 and', x, '< 8')
    else:
        print(x, '>= 8')
else:
    print(x, '<= 3')
