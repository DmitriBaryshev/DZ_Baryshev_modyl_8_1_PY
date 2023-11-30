# Задание 1
a = set((1, 3, 5, 7))
b = set((2, 4, 5, 6))
c = set((3, 5, 8, 9))
print(a.intersection(b).intersection(c))

# Задание 2
a = set((1, 3, 5, 7))
b = set((2, 4, 5, 6))
c = set((3, 5, 8, 9))

s = set(a)-set(b)-set(c)
w = set(b)-set(a)-set(c)
v = set(c)-set(a)-set(b)

print(s, w, v, sep='\n')
# Задание 3
a = (1, 2, 3, 4)
b = (1, 2, 7, 8)
c = (1, 7, 8, 1)

result = []

for i in range(len(a)):
    if a[i] == b[i] == c[i]:
        result.append(a[i])

print(result)
