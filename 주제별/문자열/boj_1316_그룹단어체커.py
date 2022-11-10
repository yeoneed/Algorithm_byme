import sys
def read_ints(): return list(sys.stdin.readline().strip())
def read_int(): return read_ints()[0]


sys.stdin = open("input.txt")


def is_valid(lst):
    group = []
    for i in range(len(lst)-1):

        if i == len(lst)-2:
            if lst[i] != lst[i+1]:
                if lst[i] in group or lst[i+1] in group:
                    return 0
                group.append(lst[i])
                group.append(lst[i+1])
                print(group)
                return 1

        if lst[i] != lst[i+1]:
            if lst[i] in group:
                return 0
            group.append(lst[i])

    return 1


def main():
    t = int(read_int())  # 문자열 몇 줄 들어오는지 입력
    cnt = 0
    for i in range(t):
        lst = read_ints()
        cnt += is_valid(lst)

    print(cnt)


if __name__ == "__main__":
    main()
