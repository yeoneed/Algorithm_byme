import sys
sys.stdin = open("input.txt")

t = int(sys.stdin.readline())

def rotate(size, tc):
    tmp = [[0 for _ in range(size)] for _ in range(size)]
    for j in range(size): #열
        for i in range(size): #행
            tmp[j][i] = tc[size-1-i][j]
    return tmp

def main():
    for t_idx in range(1, t+1):
        n = int(sys.stdin.readline())
        tc = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        result = [[0 for _ in range(n*3)] for _ in range(n)]
        tc_tmp = [[0 for _ in range(n)] for _ in range(n)]

        print(f"#{t_idx}")

        tc_90 = rotate(n, tc)
        tc_180 = rotate(n, tc_90)
        tc_270 = rotate(n, tc_180)

        #출력
        for i in range(3):
            print(''.join(map(str, tc_90[i])), end = ' ') #행은 같으니까 행 같을 때 문자열 조인하는 게 포인트!
            print(''.join(map(str, tc_180[i])), end = ' ')
            print(''.join(map(str, tc_270[i])))

if __name__ == "__main__":
    main()