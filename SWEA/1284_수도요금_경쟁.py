#import sys
#sys.stdin = open("1284.txt")

read_ints = lambda: list(map(int, input().strip().split()))
read_int = lambda: read_ints()[0]

def main():
    t = read_int()
    for t_idx in range(1,t+1):
        p,q,r,s,w = read_ints()
        case1 = p*w
        case2 = 0
        if w-r<=0:
            case2 = q
        else:
            case2 = q+(w-r)*s
        print(f"#{t_idx} {min(case1, case2)}")


if __name__ == "__main__":
    main()