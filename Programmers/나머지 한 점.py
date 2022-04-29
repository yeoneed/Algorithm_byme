import sys

coordinate = [[1,2], [3,2], [3,5]]

def solution(coordinate):
    result = []

    for i in coordinate:
        if i[0] not in result:
            result.append(i[0])
        else:
            result.remove(i[0])
        if i[1] not in result:
            result.append(i[1])
        else:
            result.remove(i[1])

    print(result)

solution(coordinate)
    