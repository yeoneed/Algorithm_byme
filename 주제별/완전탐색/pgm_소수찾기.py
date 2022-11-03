import sys
import math  # 제곱근 math.sqrt() 이용하기 위해 import
from itertools import permutations

"""
int(): 소수점 버림
math.ceil() : 소수 부분을 정수로 올려, integer로 만듭니다.
math.floor() : 소수 부분을 버리고, integer로 만듭니다.
round() : 소수 0.5 이하는 버리고, 0.5를 초과하면 올립니다.
"""


def read_ints(): return list(map(sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


def is_prime(result):  # 주어진 문자들에서 소수 판별해주는 함수
    if result[0] == '0':
        return 0

    num = int(''.join(result))
    if num == 1:  # 1은 소수아니므로 바로 0리턴
        return 0

    for i in range(2, int(math.sqrt(num))+1):  # 제곱근까지 탐색했는데도 약수가 존재하지 않으면 소수이므로 그때 1 리턴
        if num % i == 0:
            return 0
    print(num, end=" ")
    return 1


def dfs(m, lv, lst, result, visited, cnt):
    if lv == m:
        cnt += is_prime(result)
        return cnt

    lv_current = 0
    for i in range(len(lst)):
        if visited[i] == 0 and lv_current != lst[i]:
            lv_current = lst[i]
            visited[i] = 1
            result.append(lst[i])
            cnt = dfs(m, lv+1, lst, result, visited, cnt)
            result.pop()
            visited[i] = 0
    return cnt


def solution(numbers):
    lst = list(numbers)
    lst = [str(i) for i in sorted([int(i) for i in lst])]
    answer = 0
    result = []
    visited = [0] * len(lst)
    for i in range(1, len(lst)+1):
        answer += dfs(i, 0, lst, result, visited, 0)
    return answer


def main():
    numbers = sys.stdin.readline().strip()  # 문자열 입력
    print(solution(numbers))


if __name__ == "__main__":
    main()
