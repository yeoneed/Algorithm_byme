import sys

def fivo(num):
    if num<=2:
        return num
    cnt = fivo(num-1)+fivo(num-2)
    return cnt
            
            
def main():
    n = int(sys.stdin.readline()) #숫자 입력
    cnt = fivo(n)
    print(cnt)
if __name__ == "__main__":
    main()
