def print_distance(value, unit='meters'):
    print("Distance:", value, unit)

# 1 mile = 8 furlong = 1609.344 meters
print_distance(1609.344)
print_distance(8, 'furlongs') # used in horse racing.
print_distance(1, unit='mile')
