while True:
    try:
        a = int(input('key in any integer>> '))
        break
    except ValueError:
        print('\x1b[31mInvalid number!\x1b[0m')

print(f'number: {a}')
