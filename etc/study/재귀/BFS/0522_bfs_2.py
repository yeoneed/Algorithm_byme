from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid_xy(n, m, x, y):
    return x >= 0 and x < n and y >= 0 and y < m


def bfs(n, m, board, visited, src_x, src_y, dst_x, dst_y):
    size = 0
    q = deque()
    q.append((src_x, src_y, 0))
    visited[src_x][src_y] = (-2, -2)
    while q:
        x, y, l = q.popleft()
        size += 1
        if (x, y) == (dst_x, dst_y):
            return l
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid_xy(n, m, nx, ny) == 1 and visited[nx][ny] == (-1, -1) and board[nx][ny] == 1:
                q.append((nx, ny, l+1))
                visited[nx][ny] = (x, y)
    return -1


def solve(n, m, board):
    visited = [[(-1, -1) for _ in range(m)] for _ in range(n)]
    length = bfs(n, m, board, visited, 0, 0, n-1, m-1)
    if length != -1:
        history(n-1, m-1, visited)
    else:
        print(-1)


def history(x, y, visited):  # 재귀함수 생각의 흐름: 1) 여기서 뭘 출력할지, 2)다음 재귀에 뭘 넘겨 줄 것인지 3) 종료 조건
    if (x, y) == (-1, -1) or (x, y) == (-2, -2):
        return
    a, b = visited[x][y]
    history(a, b, visited)
    print((x, y))


def main():
    # case 1

    n = 15
    m = 14
    board = [
        '10000111100000',
        '11111101111110',
        '11011101101110',
        '11011101100000',
        '11011111111111',
        '11011111111100',
        '11000000011111',
        '01111111111111',
        '00000000011111',
        '01111111111000',
        '00011111111000',
        '00000001111000',
        '11111111110011',
        '11100011111111',
        '11100011111111'
    ]

    board = [list(map(int, row)) for row in board]
    solve(n, m, board)
    print()

    # case 2
    n = 5
    m = 5
    board = [
        '11000',
        '10001',
        '00101',
        '10001',
        '10111'
    ]
    board = [list(map(int, row)) for row in board]
    solve(n, m, board)


if __name__ == "__main__":
    main()
