import sys
sys.stdin = open('input.txt')

t = int(sys.stdin.readline())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0' 'C-', 'D0']

for idx in range(t):
    tc =[]
    total= []
    n,k = map(int,sys.stdin.readline().split())
    for i in range(n):
        mid,fin,hw = map(int, sys.stdin.readline().split())
        result = 0.35*mid + 0.45*fin + 0.2*hw
        total.append(result)
    
    key = total[k-1] #k번째 학생의 총점 받기
    total.sort(reverse = True) #역순 정렬
    
    grade_idx = total.index(key) // (n/10) #해당 학생 총점에 해당되는 그룹 인덱스 구하기

    print(f"#{idx} {grade[grade_idx]}")
        
    

    
