import sys

def main():
    n = int(sys.stdin.readline().strip())
    save = [-1 for _ in range(n+1)]
    save[0]=0
    save[1]=1
    for i in range(2, n+1):
        save[i] = save[i-1]+save[i-2]
    print(save[-1])
    

if __name__ == "__main__":
    main()
