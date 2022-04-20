#remove_list에 있는 거 제거하고 출력 
#lst = [i for i in range(10)]
#remove_list = set([5,7,8]) #리스트를 집합(set)으로 변환-> 시간 복잡도 줄이기 위해서 쓰는건가?(O) 그냥 리스트 써도 결과는 같음
#set은 시간 복잡도 O(1) 이고 리스트는 시간복잡도 O(n)이다. ->왜? set은 해시 함수, 해시 테이블로 구성되어 있기 때문에!
#특정 원소를 해시 함수를 통과 시킨 뒤 해당 해시가 저장소 안에 있는지 없는지 검사만 하면 된다. 그렇기에 한번의 연산, O(1)만 일어나면 된다. 
#for i in remove_list: 
    #lst.remove(i)

#lst2= [i for i in lst if i not in remove_list ] #리스트 컴프리핸션: 반복문 같은거에서 한 줄로 표현하는 것
#print(lst)
#print(lst2)

#5,7,8만 빼고 출력해보기 = lst 에서 remove_list 삭제해도 됨
lst = [i for i in range(10)]
remove_list = set([5,7,8])

for i in lst:
    if i not in remove_list:
        print(i, end= ' ')
    
lst2 = [i for i in lst if i not in remove_list]
print(lst2)

for i in remove_list:
    lst.remove(i)

print(lst)