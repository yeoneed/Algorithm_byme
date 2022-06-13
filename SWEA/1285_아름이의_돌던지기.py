#import sys
#sys.stdin = open("1285.txt")

read_ints = lambda: list(map(int, input().split()))
read_int = lambda: read_ints()[0]

def main():
    t = read_int()
    for t_idx in range(1, t+1):
        n = read_int()
        tc = read_ints()
        min_int = 1e9
        cnt = 0

        for i in tc:
            result = abs(i)
            if min_int> result:
                min_int = result
                cnt=1
            elif min_int == result:
                cnt+=1
        print(f"#{t_idx} {min_int} {cnt}")

if __name__ == "__main__":
    main()
