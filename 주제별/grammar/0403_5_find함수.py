#Hello 등장 횟수 찾기
import sys

s = "Hello, World!, Hello, Python!, Hello Zito"
cnt = 0 
idx= -1

while True:
  idx = s.find('Hello', idx+1, len(s)-1) #끝 인덱스 값까지! 이므로 기본값: len(s)-1 넣어봄
  if idx==-1: #종료 조건 명시
    break
  cnt+=1

print(cnt)

s = "Hello, World! Hello, Python!"

cnt = 0

idx = -1

#<해설>
# 문자열 hello의 횟수를 세는데 어디서 부터 탐색?- idx+1=0부터 탐색, hello가 있으면 그 hello 가 등장하는 **첫번째 인덱스** 반환
# 인덱스 없으면 -1 반환

#<find 함수 인자 설명>
# 첫번째 인자: 찾을 문자열 혹은 찾을 문자
# 두번째 인자 (생략가능): 문자를 찾을때 어디서 부터 찾을지 시작 index. 생략시 0
# 세번째 인자 (생략가능): 문자를 찾을때 어디까지 찾을지 끝 index, 생략시 문자열 맨 마지막 index= len(string)-1
