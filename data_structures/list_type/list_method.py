colors = ['red', 'green', 'black', 'cyan']

print(colors) # just print the list...

# add an item to the end of the list.
colors.append('green')
print(colors)

# add all of elements of iterable to the end of the list.
colors.extend(['orange', 'white'])
print(colors)

# insert an item to the specified position of the list.
colors.insert(2, 'blue')
print(colors)

# remove the first item that is equal to the given item.
colors.remove('cyan')
print(colors)

# delete the item given position from the list and return deleted item.
print(colors.pop(5))
print(colors)

# return the first position whose value equals given item.
print(colors.index('black'))

# return the number of given item appears in the list.
print(colors.count('green'))
print(colors.count('lapis lazuli'))

# sort the list
colors.sort()
print(colors)

# reverse the items
colors.reverse()
print(colors)

# return a shallow copy of the list
copy = colors.copy()
print(copy)

# clear all of items in the list.
colors.clear() # eqivalent to `del colors[:]`.
print(colors)
