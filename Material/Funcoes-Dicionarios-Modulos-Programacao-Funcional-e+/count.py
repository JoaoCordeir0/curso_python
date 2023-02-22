from itertools import count

c1 = count(8, 8)
# print(next(c1))
# print(next(c1))

print('c1', hasattr(c1, '__iter__'))

for i in c1:
    if i > 1000:
        break

    print(i)