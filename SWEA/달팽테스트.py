import sys
sys.stdin = open("input.txt")

dx = [0,1,0,-1] #우 하 좌 상 회전
dy = [1,0, -1, 0]

def is_valid(n,x,y):
    return x>=0 and x<n and y>=0 and y<n

def snale(n, board):
    turn = 0
    val = 2
    nx = 0
    ny = 0
    while val<=n*n:
        nx += dx[turn]
        ny += dy[turn]
        if not (is_valid(n, nx, ny)==1 and board[nx][ny]==0):
            nx-=dx[turn]
            ny-=dy[turn]
            turn+=1
            if turn>=4: turn%=4
            nx += dx[turn]
            ny += dy[turn]

        board[nx][ny] = val
        val+=1
                           
def main():
    t = int(sys.stdin.readline())
    for t_idx in range(1, t+1):
        n = int(sys.stdin.readline())
        board = [[0 for _ in range(n)] for _ in range(n)] #n*n 리스트 생성
        board[0][0] =1
        snale(n, board)
        
        print(f"#{t_idx}")
        #changed board print
        for i in board:
            for j in i:
                print(j, end = ' ')
            print()

if __name__=="__main__":
    main()