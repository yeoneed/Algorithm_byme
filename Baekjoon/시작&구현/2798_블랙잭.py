#첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
#합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
#출력: 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
#아이디어: 값을 입력받으면 조합을 다 구하고, 주어진 수 m이랑 가장 차이가 작은 조합을 고르고 그 합을 출력한다. 

import sys
from itertools import combinations
n,m = map(int, sys.stdin.readline().strip().split()) #카드 개수 n,m입력
num = list(map(int, sys.stdin.readline().strip().split())) #숫자들을 입력

result = list(combinations(num, 3)) #주어진 숫자로 만들 수 있는 모든 조합 생성

#print(result)
sum_num=[]
for k,v in enumerate(result):
    cha = m - sum(result[k]) #m과 각 인덱스 별 조합의 합의 차를 구한다. 
    if cha>=0: #그 합이 m을 넘지 않는 경우만
        sum_num.append(cha) #새로운 리스트에 저장한다.

print(m-min(sum_num)) #m에서 가장 작은 차를 뺀 것이 숫자들의 합 결과임
