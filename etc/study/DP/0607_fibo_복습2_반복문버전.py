import sys

def main():
    n = int(input())
    fibo = [-1 for _ in range(n+1)]

    for i in range(n+1):
        if i==0 or i==1:
            fibo[i] = i
        else:
            fibo[i] = fibo[i-1] + fibo[i-2]
    
    print(*fibo)

if __name__ =="__main__":
    main()