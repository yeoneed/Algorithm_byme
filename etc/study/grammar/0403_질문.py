#3 * 4의 2차원 list에 대해 row 정렬 (정렬 기준: row에서 마지막 값)
lists = [5,6,7,8]

print(lists)
print(lists[-1])

lists= sorted(lists, key = lambda lst: lst[-1]) #def func(lst): -> 인자로 5,6,7,8이 각각 넘어옴
	                                                #return lst[-1]
												#1차원: 전체 리스트 주소-> 인자 값 넘어옴
print(lists)									#2차원: 전체 리스트 주소-> 각 리스트 주소 값 넘어옴 
# 정렬 후의 결과
# [[5, 6, 4, 5],
#  [1, 9, 3, 5],
#  [5, 6, 7, 8]]

#다른 문제
num = 567
digits2 = [int(i) for i in list(str(num))]
print(digits2)
