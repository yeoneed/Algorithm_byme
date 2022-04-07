s = "Hello, World! Hello, Python!"

cnt = 0

idx = -1

while True:
  idx = s.find("Hello", idx+1) #문자열 hello의 횟수를 세는데 어디서 부터 탐색?- idx+1=0부터 탐색, hello가 있으면 그 hello 가 등장하는 첫번째 인덱스 반환, 없으면 -1 반환
# find 함수 첫번째 인자
#- 찾을 문자열 혹은 찾을 문자

#find 함수 두번째 인자 (생략가능)
#- 문자를 찾을때 어디서 부터 찾을지 시작 index. 생략시 0

#find 함수 세번째인자 (생략가능)
#- 문자를 찾을때 어디 까지 찾을지 끝 index, 생략시 문자열 맨 마지막 index

  if idx == -1: #만약 hello없어서 -1 반환됐으면
    break
  cnt += 1 #hello 있어서 인덱스 반환됐으면 cnt 증가

print(cnt) # 2