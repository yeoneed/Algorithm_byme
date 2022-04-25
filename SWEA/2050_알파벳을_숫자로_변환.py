alpha = input()

num = list(map(ord, alpha))

for i in num:
    print(i-64, end=' ')