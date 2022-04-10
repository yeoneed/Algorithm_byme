#첫째 줄에 n이, 둘째 줄에 k가 주어진다. 셋째 줄부터 n개 줄에는 카드에 적혀있는 수가 주어진다.
import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline())) #n까지 돌면서 데이터 하나씩 입력

result = list(permutations(data, k))
answer=[]

for item in result:
    answer.append(int(''.join(map(str, item))))

answer = list(set(answer))
print(len(answer))

    
