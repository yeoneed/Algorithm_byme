from collections import deque

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def is_valid_xy(n,m, start_x, start_y):
    return start_x>=0 and start_x<n and start_y>=0 and start_y<m

def bfs(n,m,board,visit, x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y]= True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==1 and visit[nx][ny]==False:
                queue.append((nx,ny))
                visit[nx][ny]=1

def solve(n, m, board):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and visit[i][j]==False:
                bfs(n,m,board,visit, i, j)
                cnt += 1
    return cnt


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
  cnt = solve(n, m, board)
  print(cnt)

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
  cnt = solve(n, m, board)
  print(cnt)

if __name__ == "__main__":
  main()