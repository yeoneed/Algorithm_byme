import sys
import math  # 제곱근 math.sqrt() 이용하기 위해 import
from itertools import permutations

"""
int(): 소수점 버림
math.ceil() : 소수 부분을 정수로 올려, integer로 만듭니다.
math.floor() : 소수 부분을 버리고, integer로 만듭니다.
round() : 소수 0.5 이하는 버리고, 0.5를 초과하면 올립니다.
"""

# 처음 오류났을 때 예외처리: 1231-> 숫자 정렬 안된경우 예제 추가 테스트
# 보완해 볼 부분: 소수 저장 배열에 넣어보고, 소수 저장 배열 set으로 선언하고 소수 저장 배열의 길이를 리턴하는 방식도 해보기!


def read_ints(): return list(map(sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


def is_prime(result):  # 주어진 문자들에서 소수 판별해주는 함수
    result = list(result)
    if result[0] == '0':
        return 0

    num = int(''.join(result))
    if num == 1:  # 1은 소수아니므로 바로 0리턴
        return 0

    for i in range(2, int(math.sqrt(num))+1):  # 제곱근까지 탐색했는데도 약수가 존재하지 않으면 소수이므로 그때 1 리턴
        if num % i == 0:
            return 0

    return 1


# set 활용한 코드
def is_prime2(nums, answer):
    # print(nums)
    for num in nums:
        if num in (0, 1) or num in answer:
            continue

        flag = 1
        # 제곱근까지 탐색했는데도 약수가 존재하지 않으면 num이 소수이므로 그때 1 리턴
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0 and i < num:
                flag = 0
                break

        if flag == 1:
            answer.add(num)
    return answer


def solution(numbers):
    lst = list(numbers)
    #lst = [str(i) for i in sorted([int(i) for i in lst])]
    answer = set()
    nums = set()
    result = []
    visited = [0] * len(lst)
    for i in range(1, len(lst)+1):
        permu_lst = list(set(permutations(lst, i)))
        for nodes in permu_lst:
            num_str = ""
            for x in nodes:
                num_str += x
            nums.add(int(num_str))
            # answer += is_prime(num_str) #인자 하나하나 소수인지 아닌지 판별
    answer = is_prime2(nums, answer)
    return len(answer)


def main():
    numbers = sys.stdin.readline().strip()  # 문자열 입력
    print(solution(numbers))


if __name__ == "__main__":
    main()
