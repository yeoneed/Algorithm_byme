import sys

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

def main():
    n = read_int()  # 숫자 입력
    arr = []
    for i in range(n):
        arr.append(read_ints())  # 2차원 배열인 원본 배열 담기

    for i in range(1, n):  # 0행 말고 1행부터 계산하기
        arr[i][0] = arr[i][0] + min(arr[i-1][1], arr[i-1][2])
        arr[i][1] = arr[i][1] + min(arr[i-1][0], arr[i-1][2])
        arr[i][2] = arr[i][2] + min(arr[i-1][0], arr[i-1][1])

    print(min(arr[n-1][0], arr[n-1][2], arr[n-1][1]))


if __name__ == "__main__":
    main()
