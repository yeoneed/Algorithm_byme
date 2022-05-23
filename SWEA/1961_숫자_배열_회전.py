#import sys
#sys.stdin = open("input.txt")

t = int(input())

def solve(size, tc, tmp):
    for j in range(size): #열
        for i in range(size): #행
            tmp[j][i] = tc[size-1-i][j]
    return tmp

def main():
    for t_idx in range(1,t+1):
        n = int(input())
        tc = [list(map(int, input().split())) for _ in range(n)]
        result = [[0 for _ in range(n*3)] for _ in range(n)]
        print(f"#{t_idx}")
        for solve_num in range(3):
            tc_tmp = [[0 for _ in range(n)] for _ in range(n)]
            tc = solve(n, tc, tc_tmp)
            for i in range(n):
                for j in range(n):
                    for k in range(solve_num, solve_num+n):
                        result[i][j] = 


if __name__=="__main__":
    main()