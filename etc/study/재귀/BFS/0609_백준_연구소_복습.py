import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

#sys.stdin = open("input_lab.txt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

def is_valid_xy(n,m, x,y):
    return x>=0 and x<n and y>=0 and y<m

def bfs(n,m,board, start):
    q = deque()
    cnt=0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for (i,j) in start:
        q.append((i,j))
        visited[i][j]=1

    while q:
        x,y = q.popleft()
        cnt+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==0 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
                board[nx][ny]=2

    return cnt #값이 2인 요소의 개수 

#def max_size(n,m,brd): #직관적이기는 하지만 시간복잡도 증가
   # cnt=0
    #for i in brd:
        #for j in i:
            #if j==0:
              #  cnt+=1
  #  return cnt

def main():
    n,m = read_ints()
    board = [read_ints() for _ in range(n)]
    zero = []
    start= []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                zero.append((i,j))
            elif board[i][j]==2:
                start.append((i,j))
            else: #기존에 벽인 요소의 개수 구하기(=cnt)
                cnt+=1

    walls = list(combinations(zero, 3)) #출력해보니 이중 튜플 형태
    min_int = 1e9
    for wall in walls: #벽 조합 별 완성된 보드에서 0인 요소의 개수 비교하기
        brd = deepcopy(board) #벽 조합 바뀔때마다 원래 보드에 적용해야 하므로 deepcopy 사용
        for (i,j) in wall:
            brd[i][j] =1
        result = bfs(n,m,brd,start)
        if min_int>result:
            min_int = result
    print(n*m - cnt-min_int-3)

if __name__ == "__main__":
    main()
