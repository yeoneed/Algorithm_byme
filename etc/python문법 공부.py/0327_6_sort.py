#lst가 주어지면 이를 정렬한 리스트를 lst2에 저장해라
import copy
lst = [5,2,3,4,6,8,9,0,1]
lst2 = copy.copy(lst)
print(sorted(lst2)) #이 버전이 더 많이 쓰임
#lst2.sort()
print(lst2)

#인자 역순으로 받아주기
for i in reversed(lst):
    print(i, end = ' ')
print()

#덧셈하는 람다 만들기
add = lambda a,b: a+b
print(5,6)

#key 값을 기준으로(오름차순), 해당하는 values 출력하기
lst = [(1, 5), (2, 4), (-5, 8), (100, -128)]

get_key = lambda k: k[0] #튜플의 첫번째 값 추출
get_value = lambda v: v[1] #튜플의 두번째 값 추출

lst2 = sorted(lst, key=get_key)#key = get_key 를 기준으로 lst를 정렬
for i in lst2:
    print(i[1], end=' ')
print()

#인자 받아 내림차순 정렬된 것으로 출력하는 lambda 구현하기
reverse_st = lambda lst: sorted(lst, reverse=True)
print(reverse_st(lst))

#아래 딕셔너리에서 key기준으로 정렬하고, 해당 value만 출력하기
d = {1: 5, 2: 4, -5: 8, 100: -128}
d_key = lambda s: s[0] #주어진 리스트에서 key 반환하도록
d2 = sorted(d.items(), key = d_key)

#for k,v in d2:
 #   print(v, end = ' ')
print([v for (k,v) in d2])#왜 리스트로 묶는거지? 딕셔너리 아니니까 값만 들어있으니까 리스트로 묶는거 같음

#0329 복습
#아래 딕셔너리에서 key기준으로 정렬하고, 해당 value만 출력하기
d = {1: 5, 2: 4, -5: 8, 100: -128}

get_key = lambda lst: lst[0]

d2 = sorted(d.items(), key = get_key)

for i in d2:
    print(i[1], end = ' ')
print()

d3 = [v for (k,v) in d2] #d.items: 튜플로 구성되어 있는 리스트 -> 호출 시 (k,v)해주면 됨
print(d3)

for k,v in d2: #d2 = d.items 랑 자료형 같음
    print(v, end=' ')