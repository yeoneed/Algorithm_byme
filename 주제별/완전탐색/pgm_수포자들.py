# 아이디어: 삼인방 패턴 저장해놓고 비교하기
# 보완해야 할 점: 배열을 다 구해야 하는 문제인가 생각해보기-> 아님, 그냥 숫자가 같은지 아닌지만 비교하면 됨-> 패턴의 길이만 구해서 배열 요소 하나하나씩 각각 비교해보기-> 인덱스 잘 사용해서 접근해보기!

def solution(answers):
    answer = []
    n = len(answers)
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a1 = a2 = a3 = 0
    for i, v in enumerate(answers):
        if v == n1[i % 5]:
            a1 += 1
        if v == n2[i % 8]:
            a2 += 1
        if v == n3[i % 10]:
            a3 += 1

    best = max(a1, a2, a3)
    if best == a1:
        answer.append(1)
    if best == a2:
        answer.append(2)
    if best == a3:
        answer.append(3)

    return answer
