digits = ["5", "6", "7"]
#num=int("".join(digits))

#print(num) # 567
#print(type(num))
#num = 567
#num = list(str(num))
#print(num)

num = 567 #기본: 숫자형 변수
ints = list(map(int, str(num)))
ints2 = list(str(num))
ints3 = [int(i) for i in ints2]

print(ints3)

ints = list(map(int, str(num)))