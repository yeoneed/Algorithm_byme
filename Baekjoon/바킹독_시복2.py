#길이 n 리스트 arr에서 합이 100인 서로 다른 위치의 두 원소가 존재하면 1, 없으면 0 반환하는 함수 func2(arr, n)작성
#arr 각 수는 0~100 n: 1000이하

def func2(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j]==100:
                return 1
    return 0

#print(func2([1,52,48], 3))
print(func2([50,42], 2))

#시복 O(n^2)