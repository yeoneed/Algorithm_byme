import sys

coordinate = [[1,2], [3,2], [3,5]]

def solution(v):
    result = []

    result.append(v[0][0]^v[1][0]^v[2][0])
    result.append(v[0][1]^v[1][1]^v[2][1])

    print(result)

solution(coordinate)