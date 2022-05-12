t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for idx in range(1,t+1):
    n,k = map(int, input().split()) #n,k 입력
    total= [] #학생 별 총점 저장하는 리스트
    for i in range(n):
        lst = list(map(int, input().split())) #학생 별 점수 입력
        total_score = 0.35* lst[0] + 0.45*lst[1] + 0.2*lst[2]
        total.append(total_score)#학생 별 총점 계산, 총점 리스트에 추가
    
    key = total[k-1] #k번째 수의 총점을 따로 저장
    total = sorted(total, reverse= True)
    #total.sort(reverse= True)와 동일

    grade_group = (total.index(key))//(n/10) #우리가 찾는 수가 몇번째 수고, 몇번째 그룹에 속하는지 구하기
    #주의: 올림 모듈 필요 없음

    print(f"#{idx} {grade[grade_group]}")


