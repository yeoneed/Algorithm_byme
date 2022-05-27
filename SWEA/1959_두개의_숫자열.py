#import sys
#sys.stdin= open("input.txt")

def ret_max(min_l, max_l,b,a):
    gap = max_l - min_l +1
    max_result = -1e9
    for i in range(gap):
        result = 0
        for j in range(min_l):
            if i+j<max_l:
                result += a[i+j]*b[j]
        if max_result<result:
            max_result = result
    return max_result

def main():
    t = int(input())
    for t_idx in range(1,t+1):
        n,m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        min_l = min(n,m)
        max_l = max(n,m)
        if len(a)<= len(b):
            min_lst = a
            max_lst = b
        else:
            min_lst = b
            max_lst = a
        
        print(f"#{t_idx} {ret_max(min_l, max_l, min_lst,max_lst)}")

if __name__ == "__main__":
    main()
