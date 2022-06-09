#각 자릿 수 리스트 만들어놓고 생각
import sys
sys.stdin = open("sample_input.txt")
def main():
    t = int(sys.stdin.readline().strip())
    for t_idx in range(1,t+1):
        is_valid = [0 for _ in range(10)]
        start_n = int(sys.stdin.readline().strip())
        cnt = 1
        while sum(is_valid)<10:
            n = start_n * cnt
            n_lst = list(str(n))
            for i in n_lst:
                if is_valid[int(i)]==0:
                    is_valid[int(i)]=1
            cnt+=1
        print(f"#{t_idx} {n}")

if __name__ == "__main__":
    main()
