#remove_list에 있는 거 제거하고 출력 
lst = [i for i in range(10)]
remove_list = set([5,7,8]) #리스트를 집합(set)으로 변환-> 시간 복잡도 줄이기 위해서 쓰는건가? 그냥 리스트 써도 결과는 같음

for i in remove_list:
    lst.remove(i)

lst2= [i for i in lst if i not in remove_list ] #리스트 컴프리핸션: 반복문 같은거에서 한 줄로 표현하는 것
print(lst)
print(lst2)
