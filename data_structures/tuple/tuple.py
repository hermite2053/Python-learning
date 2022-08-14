t1 = 10, 20, 30, 40 # separate by commas to make tuple.

print(t1[0]) # also index can be used.
print(t1) # tuple should be printed with `()`.

t2 = t1, (100, 200) # nesting
print(t2)
print(t2[0])
#t2[0][1] = 0 # tuples are immutable
