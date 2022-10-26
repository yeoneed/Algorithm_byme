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

import copy

lists = []
lists.append([5, 6, 7, 8]) # 0x10
lists.append([5, 6, 4, 5]) # 0x20
lists.append([1, 9, 3, 5]) # 0x30

lists = [0x10, 0x20, 0x30]
#case1: 얕은 복사
list2 = copy.copy(lists)  # [0x10, 0x20, 0x30]- 같은 주소에 저장
#case2: 깊은 복사
list2 = copy.deepcopy(lists)  # [5678->0x40, 5645->0x50, 1935->0x60] - 새로운 주소에 저장

#case1: 0x10번지의 [0]값-> lists의 5와 list2의 5 둘다 6으로 변경됨
#case2: 0x40번지의 [0]값-> list2의 5만 6으로 변경 
list2[0][0] += 1

#일차원 리스트는 deepcopy 안해도 됨-> 1차원은 주소를 copy하는게 아니라 바로 값을 copy하는 듯
lists = [5, 6, 7, 8]  # 5, 6, 7, 8  0x100
lists2 = copy.copy(lists) # 0x200 5, 6, 7, 8