#N이 주어질 때 a, b, c, d, e 를 출력하라.
import sys
sys.stdin = open("input.txt")

def main():
    t = int(sys.stdin.readline())
    for t_idx in range(1,t+1):
        cnt = [0,0,0,0,0]
        quo = [2,3,5,7,11]
        num = int(sys.stdin.readline())
        print(f"#{t_idx}", end = ' ')
        for i in range(5):
            while num%quo[i]==0:
                num//= quo[i]
                cnt[i]+=1
        print(*cnt)

if __name__ == "__main__":
    main()
