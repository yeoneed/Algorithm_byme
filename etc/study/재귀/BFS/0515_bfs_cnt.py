from collections import deque
dx= [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m, x,y):
    return x>=0 and x<n and y>=0 and y<m

def bfs(n,m,board,visited,x,y):
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    size = 0
    while q:
        x,y = q.popleft()
        size += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
    return size

def solve(n, m, board):
    size = []
    cnt = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and visited[i][j]==0:
                size.append(bfs(n,m,board,visited,i,j))
                cnt+=1
    return cnt, sorted(size)

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
  cnt, sizes = solve(n, m, board)
  print(cnt, sizes)

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
  cnt, sizes = solve(n, m, board)
  print(cnt, sizes)

if __name__ == "__main__":
  main()