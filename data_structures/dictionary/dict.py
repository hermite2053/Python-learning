greek = {'alpha': 1, 'beta': 2, 'gamma': 3}

greek['delta'] = 4 # add a key and coressponding value
print(greek)

del greek['beta'] # delete item
print(greek)

print(list(greek)) # return list of the dicitonary
print(sorted(greek)) # return a new sorted instance of the iterable
print(len(greek)) # return the number of items in the dictionary
print(greek.get('delta')) # return the value coressponding given key

print('alpha' in greek) # testing
print('zeta' in greek) # testing
