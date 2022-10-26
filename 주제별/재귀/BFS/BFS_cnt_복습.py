from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m,x,y):
    return x>=0 and x<n and y>=0 and y<m

def bfs(n,m,board,visited,start_x,start_y):
    q = deque()
    q.append((start_x,start_y))
    visited[start_x][start_y]=1 #큐에 넣으면 바로 방문처리, 그 점 기준으로 탐색 또 하겠다는 소리니까
    size = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
                size+=1 #큐에 상하좌우 탐색해서 다른 거 들어오는 순간 섬의 사이즈 증가시키기
    return size

def solve(n, m, board):
    cnt = 0
    sizes = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]== 1 and visited[i][j] ==0:
                size = bfs(n,m,board,visited,i,j) #각 섬의 사이즈 반환받음
                sizes.append(size) #사이즈 값 저장하는 리스트에 각 섬의 사이즈 저장함
                cnt+=1 #bfs 호출될 때 마다 증가(섬 개수 세기)
    return cnt, sorted(sizes)
    
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