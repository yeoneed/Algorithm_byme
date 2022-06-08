import sys
sys.stdin = open("sample_input.txt")

def solve(start_n, lst, cnt):
    n = start_n * cnt
    n_lst = list(str(n))
    for i in n_lst:
        if i not in lst:
            lst.append(i)
    lst_int = list(map(int, lst))
    if 0 in lst_int and sum(lst_int)==45:
        return n
    result = solve(start_n, lst,cnt+1) #계속 같은 결과 반환하고 싶으므로 result 변수에 저장, 반환
    return result

def main():
    t = int(sys.stdin.readline().strip())
    for t_idx in range(1,t+1):
        lst = []
        n = int(sys.stdin.readline().strip())
        print(f"#{t_idx} {solve(n, lst, 1)}")

if __name__ == "__main__":
    main()