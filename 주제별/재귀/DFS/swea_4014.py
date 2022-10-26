#import sys
def read_ints(): return list(map(int, input().split()))
def read_int(): return read_ints()[0]


#sys.stdin = open("input.txt")


def check_slope(row, N, X):
    cnt = 1  # 경사로 세울 수 있는 경우의 수
    for i in range(1, N):
        if row[i] == row[i-1]:  # 같은 높이라면 거리 증가
            cnt += 1
        elif row[i] - row[i-1] == 1 and cnt >= X:   # 높이 1 높아지면
            cnt = 1
        elif row[i-1] - row[i] == 1 and cnt >= 0:   # 높이 1 낮아지면
            cnt = -X + 1
        else:   # 높이 2 이상 차이나면
            return 0
    if cnt >= 0:
        return 1
    return 0


def main():
    T = int(input())
    for tc in range(1, T+1):
        N, X = read_ints()
        board = []
        result = 0
        for i in range(N):
            board.append(read_ints())
            result += check_slope(board[i], N, X)

        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(board[j][i])
            result += check_slope(temp, N, X)

        print(f"#{tc} {result}")


if __name__ == "__main__":
    main()
