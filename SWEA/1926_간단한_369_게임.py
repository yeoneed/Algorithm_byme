num = int(input())

for i in range(1,num+1):
    count=0
    i = str(i)
    lsti = "".join(i)
    for idx,v in enumerate(lsti): 
        if v == '3' or v=='6' or v=='9':
            count+=1
    if count:
        print('-'*count, end=' ')
    else:
        print(i, end=' ')

#숫자를 문자 형태로 바꿔서 리스트에 저장하고 리스트를 돌면서 3,6,9의 개수만큼 '-'를 세기 위해 3,6,9의 개수인 count 변수를 사용
#0506: 내일 정처기 시험인 관계로 코테 하루만 휴식