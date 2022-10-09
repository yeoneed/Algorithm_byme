import sys
from collections import deque

sys.stdin = open("beer.txt")


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


def bfs(st_x, st_y, dst_x, dst_y, q):
    flag = 1
    while q:
        x, y = q.popleft()  # 집과 첫번째 가게 사이의 거리 구하기 위해
        if (abs(x-st_x) + abs(y-st_y))/50 > 20:
            flag = -1
        else:
            st_x = x
            st_y = y

    if (abs(dst_x-st_x) + abs(dst_y-st_y))/50 > 20:
        flag = -1

    return flag


def main():
    t = read_int()
    for i in range(t):
        store_num = read_int()
        q = deque()
        h_x, h_y = read_ints()

        for i in range(store_num):
            s_x, s_y = read_ints()
            q.append((s_x, s_y))  # 가게 리스트에 가게 좌표들 저장

        f_x, f_y = read_ints()
        if bfs(h_x, h_y, f_x, f_y, q) == 1:
            print("happy")
        else:
            print("sad")


if __name__ == "__main__":
    main()
