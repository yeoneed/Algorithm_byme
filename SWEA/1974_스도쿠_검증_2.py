import sys
sys.stdin = open("input.txt")

t = int(sys.stdin.readline())

def solve(tc):
    result = 1
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                if tc[i][j] == tc[i][k]:
                    return 0
                elif tc[j][i]== tc[k][i]:
                    return 0

    for i in range(3):
        for j in range(3):
            cnt = [0 for _ in range(0,10)] #9개의 수 사용했는 지 안했는 지 체크하기 위한 리스트 생성
            for k in range(3):
                for l in range(3):
                    if cnt[tc[i*3+k][j*3+l]]>=1:
                        return 0
                    else:
                        cnt[tc[i*3+k][j*3+l]]+=1

    return result

def main():
    for t_idx in range(1,t+1):
        tc = [list(map(int, sys.stdin.readline().split())) for _ in range(9)] #testcase 입력
        answer = solve(tc)
        print(f"#{t_idx} {answer}")
        
if __name__ == "__main__":
    main()
