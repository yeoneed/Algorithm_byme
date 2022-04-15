lst = [i for i in range(10)]
lst2 = []
#for i in range(len(lst)): #맨날 계산하는 거 아니고, 갖고 오는거임
#for i, val in enumerate(lst):#enumerate 형태로 갖고옴
    # print(i,':', lst[i])
   # print(f"{i} : {lst[i]}")

#lst2 = lst[1:5] #append대신 사용 (범위는 range(a,b)와 동일)

#print(lst2)

#for i in lst:
#    if i!=5:
#        lst2.append(i)
#from copy import copy

#lst2 = copy(lst)
#lst2.remove(5) #값 접근 시는 remove 함수 사용
#print(lst2)
#print(lst)

#lst3 = lst[:5] + lst[6:] #인덱스 접근 시: slicing 접근
#print(lst3)
#간단한 프로젝트에서도 기술 근거를 달면 된다. -> 예를 들어 게시판 사용-> 디비 사용 멀티프로세스 멀티 쓰레드 시간 다 측정해보고 왜 멀티 쓰레드를 사용하는건지 이런식으로!


remove_list = set([5,7,8]) #왜 리스트 대신 set을 써주는거지? : 중복 제거, 해시테이블 사용해서 시간복잡도 O(1)
for i in remove_list:
    lst.remove(int(i))

lst2 = [i for i in lst if i not in remove_list] #O(n)*1-> not in 이 set에서는 시간복잡도 O(1)

print(lst2)