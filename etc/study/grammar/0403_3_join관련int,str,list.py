digits = ["5", "6", "7"]
#num=int("".join(digits)) #"구분자".join(리스트)형태, join안에는 무조건 list형태가 들어가야함

#print(num) # 567
#print(type(num)) -> int
#num = 567
#num = list(str(num))
#print(num)

num = 567 #기본: 숫자형 변수
ints = list(map(int, str(num))) #num의 인자 각각 문자열로 바꿔서 리스트에 집어넣으려는데, 이 인자를 문자열이 아니라 int로 하겠다~
ints2 = list(str(num))#'5', '6', '7'
#ints3 = [int(i) for i in ints2]

print([int(i) for i in ints2])

#ints = list(map(int, str(num)))