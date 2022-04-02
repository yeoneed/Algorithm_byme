# 수가 666에서 증가하면서 666이 있는 것만 세고, n이랑 count한 수랑 같으면 그 수를 출력
import sys
n = int(sys.stdin.readline().strip())
cnt =0
s = '666'

while True:
    if '666' in s: #666이 주어진 문자열에 들어있으면
        cnt+=1 #666이 들어있는 경우를 하나 증가시킴
        if cnt == n: #경우의 수가 n번째랑 같으면 
            print(s) #그 문자열을 출력
            break
    s = str(int(s)+1) #666에서 숫자 하나씩 증가시킴 




