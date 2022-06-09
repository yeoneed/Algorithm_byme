import sys
from collections import deque
sys.stdin = open("input_tomato.txt")

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m,x,y):
    return x>=0 and x<n and y>=0 and y<m

def bfs(n,m,start, board, valid_num): #너비우선 탐색으로 1인 좌표의 상하좌우 중 0인 좌표를 다 1로 바꾼다. 
    visited = [[0 for _ in range(m)] for _ in range(n)]

    cnt=0
    q = deque()
    for (i,j) in start:
        q.append((i,j, 0)) #시작이 1인 좌표값들 모두 큐에 넣고 방문 처리
        visited[i][j] =1

    while q:
        x,y, step = q.popleft()
        cnt+=1
        if cnt==valid_num:
            return step
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and visited[nx][ny]==0 and board[nx][ny]==0:
                q.append((nx, ny, step+1))
                visited[nx][ny]=1  

    return -1

def main():
    m,n = read_ints()
    board = [read_ints() for _ in range(n)] #입력 완료
    
    start= []
    valid_num = int(m) * int(n)
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                start.append((i,j)) #시작점에 추가
            elif board[i][j]==-1:
                valid_num-=1

    result = bfs(n,m,start,board,valid_num)
    print(result)

if __name__ == "__main__":
    main() 
