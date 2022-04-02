# enumerate 사용
lst = [i for i in range(10)]
for i,val in enumerate(lst): #인덱스 구해야 할 때: 의식적으로 이 반복문 사용하기 + for문에서 가급적 range 사용하지 말기!
    print(f"{i}:{lst[i]}")
    #print(i, ':', lst[i])랑 같음


#인덱스, 값 동시에 구하기 복습
lst = [i for i in range(10)]
for k,v in enumerate(lst):
    print(f"{k} : {lst[k]}")
