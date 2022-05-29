#문제: 리스트가 주어지면 리스트 원소끼리 나눴을 때 그 나머지의 합을 모두 더하기
#예시) 3 7 5 8에서 총 3%7 = 3, 3%8=3, 5%3=2..... 다 더하면 합이 37

#import sys
#sys.stdin = open("input.txt")

t = int(input())

def remain(tc,n):
    result = 0
    for i in range(n):
        for j in range(n):
           result += tc[i]%tc[j]
    return result

def main():
    for t_idx in range(1, t+1):
        n = int(input())
        tc = list(map(int, input().split()))
        answer = remain(tc,n)
        print(f"#{t_idx} {answer}")
        
if __name__ == "__main__":
    main()


    
    