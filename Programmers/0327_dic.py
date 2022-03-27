d = {'a': 1, 'b': 2, 'c': 3}

print(d['c'])
print(d.get('e', 0))

for k in d.keys():
    print(k, end=" ")
print()

for v in d.values():
    print(v, end=" ")
print()

for k in d.keys():
    print(f"{k}: {d[k]}")

for k, v in d.items():
    print(f"{k}: {v}")

d2 = dict([(v, k) for k, v in d.items()])
print(d2)

tmp = dict()
s = set()

s.add(5)
print(5 in s)