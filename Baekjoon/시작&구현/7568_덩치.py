#입력:#첫 줄에는 전체 사람의 수 N이 주어진다. 
# 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
#출력: 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 
# 단, 각 덩치 등수는 공백문자로 분리되어야 한다.
import sys
n = int(sys.stdin.readline()) #사람 수
s = list() #리스트 선언 요렇게?
cnt =[1 for _ in range(n)] #1이 n개 저장되어 있는 리스트
#print(cnt)

for _ in range(n):
    x,y = map(int, sys.stdin.readline().strip().split()) #n개의 줄에 (x,y)입력
    s.append((x,y)) #s 리스트에 (x,y)추가

for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i][0] > s[j][0] and s[i][1] > s[j][1]: #더 큰 숫자 존재하면
            cnt[j]+=1 #카운트 증가
        elif s[i][0] <s[j][0] and s[i][1] < s[j][1]:
            cnt[i]+=1 

for i in cnt:
    print(i, end= ' ')

        
