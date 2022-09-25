def reverse_str(str):
    for ch in range(len(str)-1, -1, -1):
        yield str[ch]

    return str


s = 'Python'
print(s)
for ch in reverse_str(s):
    print(ch)

t = 'semordnilap'
print(t)
for ch in reverse_str(t):
    print(ch)
