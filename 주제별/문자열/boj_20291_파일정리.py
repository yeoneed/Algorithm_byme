import sys
# 딕셔너리 사용하는 문제


def read_ints(): return list(sys.stdin.readline().strip().split('.'))


sys.stdin = open("input.txt")


def main():
    t = int(sys.stdin.readline().strip())
    result = {}

    for i in range(t):
        name, ftype = read_ints()
        if ftype not in result:
            result[ftype] = 1
        else:  # 한번이상 나왔던 알파벳이라면
            result[ftype] += 1  # 해당 문자의 등장 횟수 배열에 1 추가

    result = sorted([(k, v)
                    for k, v in result.items()], key=lambda x: x[0])

    for k, v in result:
        print(f"{k} {v}")


if __name__ == "__main__":
    main()
