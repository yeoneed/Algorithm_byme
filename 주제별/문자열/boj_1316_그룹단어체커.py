import sys
# 첫번째 람다 함수: 공백 기준 없이 요소 하나씩 리스트에 담음!!
def read_ints(): return list(sys.stdin.readline().strip())
# 위에서 .split()안해주면 10들어올때 1만 들어오기 때문에 입력 새로 받아야함
#def read_int(): return read_ints()[0]

#sys.stdin = open("input.txt")


def is_valid(lst):
    # print(lst)
    group = []

    for i in range(len(lst)-1):
        # print(lst[i])
        if lst[i] != lst[i+1]:
            if lst[i] in group:
                return 0
            group.append(lst[i])

    if lst[-1] != lst[len(lst)-2]:
        if lst[-1] not in group:
            return 1
        else:
            return 0
    else:
        if lst[-1] in group:
            return 0

    return 1


def main():
    t = int(sys.stdin.readline().strip())
    # print(t)
    cnt = 0
    for i in range(t):
        lst = read_ints()
        cnt += is_valid(lst)

    print(cnt)


if __name__ == "__main__":
    main()
