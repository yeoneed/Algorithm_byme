import copy 
lst = [5, 2, 4, 8, 1, 6, 7, 3, 2, 9, 0]
#lst2 = copy.copy(lst)
#lst2.sort()#리스트에서 제공하는 메소드 
lst2 = sorted(lst)#파이썬 메소드
print(lst2)
print(lst)

for i in reversed(lst):#인자를 역순으로 받아줌
    print(i, end=" ")
print()

add = lambda a, b: a + b #lambda = 함수 호출을 간단하게
print(add(5, 6))

lst = [(1, 5), (2, 4), (-5, 8), (100, -128)]
get_x = lambda a: a[0]
get_y = lambda a: a[1]
print(sorted(lst, key=get_x)) #key 값을 기준으로 값 정렬- lst의 인자들이 get_key에 들어감
print(sorted(lst, key=get_y)) #key 값을 기준으로 y 정렬(위의 정의를 바탕으로)

reverse_sorted = lambda x: sorted(x, reverse=True)#-> lst의 첫번째 인자를 기준으로 역순 정렬

reverse_sorted(lst)
#key 정렬-> 해당 value 를 출력
d = {1: 5, 2: 4, -5: 8, 100: -128}
print(d)
print(d.items())

get_key = lambda i: i[0]

sorted_kv = sorted(d.items(), key=get_key)#key -> lambda 에서 받은 기준 값
print([v for k, v in sorted_kv])