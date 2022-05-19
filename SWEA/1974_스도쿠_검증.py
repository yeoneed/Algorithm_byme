import sys
sys.stdin = open('input.txt')
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

    for r_idx in range(3):
        for c_idx in range(3):
            for i in range(3*r_idx, 3*r_idx+3):
                for j in range(3*c_idx, 3*c_idx+3):
                    for k in range(i, 3*r_idx+3):
                        for l in range(j, 3*c_idx+3):
                            if k!=i and l!=j and tc[i][j]==tc[k][l]:
                                return 0
    return result


def main():

    for t_idx in range(1,t+1):
        tc = [list(map(int, sys.stdin.readline().split())) for _ in range(9)] #9*9 리스트 선언

        answer = solve(tc)
        print(f"#{t_idx} {answer}")

if __name__ == "__main__":
  main()


#코멘트: 해당 숫자 개수 세는 리스트 추가해서 다시 구현해보기!
#내 코드 시간 복잡도가 안 좋을듯,,