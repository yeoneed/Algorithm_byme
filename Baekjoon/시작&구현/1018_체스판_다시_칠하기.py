#첫째 줄에 N과 M이 주어진다. 
# N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
#첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
import sys
n,m = map(int, sys.stdin.readline().strip().split())
s = []

for i in range(n):
    s.append(sys.stdin.readline().split())

for i in range(n):
    s[i] = str(s[i]).strip('[')
    s[i] = s[i].strip(']')
    s[i]=list(s[i])
    s[i] = s[i][1:m+1]

s_cnt = [[0 for _ in range(m)] for _ in range(n)] #s크기와 동일한 0으로 채워진 리스트 입력받기

if s[0][0]=='B': #첫자리 수 B일때 자리에 안맞게 들어가 있는 것의 개수 세기
    for i in range(n):
        for j in range(m): 
            if (i+j)%2==0:
                
elif s[0][0]=='W': #첫자리 수 W일때 자리에 안맞게 들어가 있는 것의 개수 세기
     for i in range(n):
        for j in range(m):
            if i%2==0 and j%2==1:
                if s[i][j]!='B': s_cnt[i][j] +=1
            elif i%2==0 and j%2==0:
                if s[i][j]!='W': s_cnt[i][j]+=1
            elif i%2==1 and j%2==1:
                if s[i][j]!='W': s_cnt[i][j] +=1
            elif i%2==1 and j%2==0:
                if s[i][j]!= 'B': s_cnt[i][j] +=1

#print(s_cnt)
res = []
sum_s=0

for t in range(n-7):
    for i in range(t, t+8):
        for j in range(t, t+8):
            sum_s += s_cnt[i][j]
            if sum_s!=0:
                res.append(sum_s)

print(min(res))
