#copy 사용해서 문자열 변경하는 예제
import copy #copy 라이브러리 
# from copy import copy -> copy 라이브러리에 있는 copy 메소드 불러오기
lst = [i for i in range(10)]
lst2= copy.copy(lst)
lst2.remove(5) #<값!!>을 변경할 때는 remove 사용
print(lst2)
print(lst)
lst3 = lst[:5] + lst[6:]
print(lst3) #<인덱스!!(5)> 빼고 출력 시는 slice 사용
