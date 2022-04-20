import sys

s = [i for i in range(1,21)] #1부터 20까지 저장
read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))

def rev(a,b):
    i=0
    while a+i<b-i:
        s[a+i], s[b-i] = s[b-i], s[a+i]
        i+=1
    return s   


def main():
    for i in range(10):
        interval = read_ints()
        x = interval[0]
        y= interval[1]
        s = rev(x-1,y-1)

    for i in s:
        print(i, end = ' ')

if __name__ == "__main__":
  main()        