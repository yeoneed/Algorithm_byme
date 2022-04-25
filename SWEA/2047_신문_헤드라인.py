headline = input()

head_lst= list(headline)

for i,v in enumerate(head_lst):
    if ord(v)>=97 and ord(v)<=122:
        head_lst[i] = chr(ord(v)-32)

print(''.join(head_lst))