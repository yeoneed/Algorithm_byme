import sys

sys.stdin = open("input.txt")

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

def dp(n,m, board):
    save = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                save[i][j] = board[i][j]
            elif i==0:
                save[i][j] = save[i][j-1] + board[i][j]
            elif j==0:
                save[i][j] = save[i-1][j] + board[i][j]
            else:
                save[i][j] = max(save[i-1][j], save[i][j-1], save[i-1][j-1]) + board[i][j]
    return save[n-1][m-1]

def main():
    n,m = read_ints()
    board = [read_ints() for _ in range(n)]
    print(dp(n,m,board))

if __name__ == "__main__":
    main()