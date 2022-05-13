#import sys

#sys.stdin = open('input.txt')


t = int(input())

for idx in range(1,t+1):
    tc = []
    total_cnt = 0

    n,k = map(int, input().split())
    for i in range(n):
        tc.append(list(map(int, input().split())))
    
    for i in range(n): #가로, 세로 탐색
        cnt1=0 #한 라인 셀 때 마다 변수들 초기화
        cnt2=0 
        max1=0 
        max2=0
        for j in range(n): #가로로 탐색
            if tc[i][j]==0:
                if max1==k:
                    total_cnt+=1
                cnt1=0
                max1=0
            else:
                cnt1+=1
                if max1<cnt1:
                    max1=cnt1

            if tc[j][i]==0: #세로로 탐색
                if max2==k:
                    total_cnt+=1
                cnt2=0
                max2=0
            else:
                cnt2+=1
                if max2<cnt2:
                    max2=cnt2

        if max1==k:
            total_cnt+=1
        if max2==k:
            total_cnt+=1
    
    print(f"#{idx} {total_cnt}")