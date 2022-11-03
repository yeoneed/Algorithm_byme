import sys


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


# 리스트 굳이 안써도 되는 경우는 쓰지 말기-> 바로 비교 때리기
def solution(sizes):
    width = 0
    height = 0
    for lens in sizes:
        w = lens[0]
        h = lens[1]
        if w < h:
            w, h = h, w  # 파이썬에서는 이 한 줄로 swap이 된다.
        width = max(w, width)
        height = max(h, height)

    answer = width * height
    return answer


def main():
    sizes = []
    for i in range(5):
        sizes.append(read_ints())
    print(solution(sizes))


if __name__ == "__main__":
    main()
