#- dictionary에서 key만 출력
    
d = {'a': 1, 'b': 2, 'c': 3}

for i in d.keys():
    print(i, end= ' ')
print()

for v in d.values():
    print(v, end= ' ')

for k,v in d.items():
    print()