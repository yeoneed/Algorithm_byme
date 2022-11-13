import sys
# 문제에서 배운 것: 꼭 길이먼저 정렬하지 않아도 됨!!! 알파벳 먼저 정렬하고 길이 정렬하는게 더 빠름,,


sys.stdin = open("input.txt")

"""
def solution(word_lst):
    word_lst = sorted([(k, v) for k, v in word_lst],
                      key=lambda x: x[0])  # 알파벳 순 정렬
    word_lst = sorted([(k, v) for k, v in word_lst],
                      key=lambda x: x[1])  # 길이 순 정렬

    for k, v in word_lst:
        print(k)
"""


def main():
    t = int(sys.stdin.readline().strip())  # 문자열 몇 줄 들어오는지 입력
    word_lst = []

    for i in range(t):
        word = sys.stdin.readline().strip()
        word_lst.append(word)
        # word_lst.append((word, len(word))) #lambda ver
    word_lst = list(set(word_lst))
    # solution(word_lst) lambda ver
    word_lst = list(set(word_lst))  # 중복제거-> 문자열 들어올때 마다 하지않고, 한번만 해야 시간초과 안남
    word_lst.sort()
    word_lst.sort(key=len)

    for word in word_lst:
        print(word)


if __name__ == "__main__":
    main()
