# 6001
print("Hello")

# 6002
print("Hello World")

# 6003
print("Hello\nWorld")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print("\"!@#$%^&*()\'")

#6007
print("\"C:\\Download\\'hello'.py\"")

#6008
print('print("Hello\\nWorld")')

#6009
a = input()
print(a)

#6010
a = input()
a = int(a)
print(a)

#6011
a=input()
a = float(a)
print(a)

#6012
a = input()
b = input()
print(a)
print(b)

#6013
a = input()
b = input()
print(b)
print(a)

#6014
a = input()
print(a)
print(a)
print(a)

#6015
a,b = input().split()
print(a)
print(b)

#6016
a,b = input().split()
print(b,a)

#6017
s = input()
print(s,s,s)

#6018
h,m = input().split(':')
print(h,m,sep=':')

#6019
y,m,d = input().split('.')
print(d,m,y,sep='-')

#6020
l,r = input().split('-')
print(l,r,sep='')

#6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#6022
ymd = input()
print(ymd[0:2])
print(ymd[2:4])
print(ymd[4:6])

#6023
s = input().split(':')
print(s[1])

#6024
a,b = input().split()
s = a+b
print(s)

#6025
a,b = input().split()
r = int(a) + int(b)
print(r)

#6026
a = input()
b = input()
s = float(a)+float(b)
print(s)

#6027
a = input()
b = int(a)
print('%x'%b)

#6028
a = input()
n = int(a)
print('%X'%n)

#6029
a = input()
n = int(a,16)
print('%o'%n)

#6030
n = ord(input())
print(n)

#6031
c = int(input())
print(chr(c))

#6032
c = int(input())
print(-c)

#6033
a = ord(input())
print(chr(a+1))

#6034 - 주의*
a,b = input().split()
c= int(a) - int(b)
print(c) 

#6035
a,b = input().split()
m = float(a)*float(b)
print(m)

#6036
w, l = input().split()
print(w * int(l))

#6037
#반복 횟수와 문장이 줄을 바꿔 입력된다.
n = input()
s = input()
print(int(n)*s)

#6038
#정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a, b = input().split()
c = int(a)**int(b)
print(c)

#6039
a,b = input().split()
c = float(a)**float(b)
print(c)

#6040
a,b = input().split()
print(int(a)//int(b))

#6041
a,b = input().split()
s= int(a)%int(b)
print(s)

#6042
a = float(input())
print(format(a,".2f"))

#6043
f1,f2 = input().split()
s = float(f1)/float(f2)
print(format(s,".3f"))

#6044
a,b = input().split()
x= int(a)
y = int(b)
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x%y)
print(format(float(a)/float(b),".2f"))

#6045
#합과 평균을 공백을 두고 출력한다. 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
a,b,c = map(int, input().split())
sum = a+b+c
avg = format(sum/3, ".2f")
print(sum, avg)

#6046
a = int(input())
print(a<<1)

#6047
a, b = map(int, input().split())
print(a<<b)

#6048
a,b = map(int, input().split())
print(a<b)

#6049
a,b = map(int, input().split())
print(a==b)

#6050
a,b = map(int, input().split())
print(a<=b)

#6051
a,b = map(int, input().split())
print(a!=b)

#6052
a = int(input())
print(bool(a))

#6053
a = bool(int(input()))
print(not a)

#6054
a,b = map(int, input().split())
print(bool(a) and bool(b))

#6055
a,b = map(int, input().split()) #map 함수의 기능: (적용시킬 함수, 함수를 적용할 값) 
print(bool(a) or bool(b))

#6056
a,b = map(int, input().split())
a = bool(a)
b = bool(b)
print((a and (not b)) or ((not a) and b))

#6057
a,b = map(int, input().split())
a = bool(a)
b = bool(b)
print(a==b)

#6058
a,b = input().split()
a = bool(int(a))
b= bool(int(b))
print(not(a or b))

#6059
a = int(input())
print((~a))

#6060
a,b = map(int, input().split())
print(a&b)

#6061
a,b = map(int, input().split())
print(a|b)

#6062
a,b = map(int, input().split())
print(a^b)

#6063
a, b = map(int, input().split())
c = (a if(a>b) else b)
print(c)

#6064
a,b,c = map(int, input().split())
result = ((b if(b<a) else a) if(a<c) else (b if(b<c) else c))
print(result)

#6065
a,b,c = map(int, input().split())
if a%2==0:
 print(a)

if b%2==0:
 print(b)

if c%2==0:
 print(c)

#6066
 a,b,c= map(int, input().split())
if a%2==0:
    print("even")
else:
    print("odd")
    
if b%2==0:
    print("even")
else:
    print("odd")
    
if c%2==0:
    print("even")
else:
    print("odd")

#6067
a = int(input())
if a>0:
    if a%2==0:
        print("C")
    else:
        print("D")
elif a<0:
    if a%2==0:
        print("A")
    else:
        print("B")

#6068
a = int(input())
if a>=90 and a<=100:
    print("A")
elif a>=70 and a<90:
    print("B")
elif a>=40 and a<70:
    print("C")
elif a>=0 and a<40:
    print("D")

#6069
a = input()
if a=='A':
    print("best!!!")
elif a=='B':
    print("good!!")
elif a=='C':
    print("run!")
elif a=='D':
    print("slowly~")
else:
    print("what?")

#6070
a = int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")

#6071
a = int(input())

while a!=0:
    print(a)
    a = int(input())
#6071-ver2
while True:
    a = int(input())
    if a==0:
        break
    else:
        print(a)

#6072
a = int(input())
while a!=0:
    print(a)
    a = a-1
#6072-ver2
a = int(input())
while True:
    if a==0:
        break
    else:
        print(a)
        a = a-1

#6073
a = int(input())

while a!=0:
    print(a-1)
    a = a-1
#6073-ver2
a = int(input())

while a>=1:
    print(a-1)
    a = a-1
#6073-ver3
a = int(input())
while a!=0:
  a = a-1
  print(a)

#6074
n = ord(input())
a = ord('a')
while a<=n:
    print(chr(a))
    a= a+1

#6075
n = int(input())
a = 0
while a<=n:
    print(a)
    a+=1
