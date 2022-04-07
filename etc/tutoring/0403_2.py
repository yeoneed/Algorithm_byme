import copy
lists = []
lists.append([5, 6, 7, 8])
lists.append([5, 6, 4, 5])
lists.append([1, 9, 3, 5])

print(lists)
# [[5, 6, 7, 8],
#  [5, 6, 4, 5],
#  [1, 9, 3, 5]]

lists2 = copy.deepcopy(lists) #깊은 복사: 주소를 따로 지정
#얕은 복사: 주소 같은 곳에 있음

print(lists2)
# [[5, 6, 7, 8],
#  [5, 6, 4, 5],
#  [1, 9, 3, 5]]

lists2[0][0] += 1
print(lists)
# [[5, 6, 7, 8],
#  [5, 6, 4, 5],
#  [1, 9, 3, 5]]

print(lists2)
# [[6, 6, 7, 8],
#  [5, 6, 4, 5],
#  [1, 9, 3, 5]]