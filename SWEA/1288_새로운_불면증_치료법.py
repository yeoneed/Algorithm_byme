import sys
sys.stdin = open("sample_input.txt")

def solve(start_n): #n=1295
    n = start_n
    cnt = 1
    lst = []
    while True:
        n_lst = list(str(n))
        for i in n_lst:
            if i not in lst: #1 2
                lst.append(i)       
        lst_int = list(map(int, lst))
        if sum(lst_int)==45 and 0 in lst_int:
            return n
        cnt+=1
        n = start_n*cnt

def main():
    cnt = 0
    t = int(sys.stdin.readline().strip())
    for t_idx in range(1,t+1):
        n = int(sys.stdin.readline().strip())
        print(f"#{t_idx} {solve(n)}")

if __name__ == "__main__":
    main()