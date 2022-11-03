import sys
from collections import deque

# 생각: <을 만나면 그 전까지 스택에 있는 거 다 pop하고 <안에 등장하는 애들을 출력한다.
# >을 만나면 그 전까지 스택==데크에 있는거 다 popleft() 한다
# 파이썬에서는 list 가 이미 deq 형태임
# 공백 만나면 여지까지 스택에 들어있던 거 다 출력


def read_ints(): return list(sys.stdin.readline().strip())


sys.stdin = open("input.txt")


def main():
    s = read_ints()
    deq = deque()
    flag = 0
    for name in s:
        if (name >= 'a' and name <= 'z') or (name >= '0' and name <= '9'):
            deq.append(name)
        elif name == ' ':
            if flag == 0:
                while deq:
                    print(deq.pop(), end='')
                print(name, end='')
            else:
                while deq:
                    print(deq.popleft(), end='')
                print(name, end='')
        elif name == '<':
            flag = 1
            while deq:
                print(deq.pop(), end='')
            print(name, end='')
        elif name == '>':
            flag = 0
            while deq:
                print(deq.popleft(), end='')
            print(name, end='')
    while deq:  # 남은 애들 출력
        print(deq.pop(), end='')


if __name__ == "__main__":
    main()
