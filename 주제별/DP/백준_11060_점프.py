import sys

sys.stdin = open("input.txt")

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

def dp(n,lst):
    cnt = 0
    for i in range(n):
        for j in range(i,lst[i]+1):
            if i+j<n:
                


def main():
    n = read_int()
    lst = read_ints()
    print(dp(n,lst))
    
if __name__ == "__main__":
    main()

#면접 끝나고 꼭 복습하기