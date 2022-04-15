#조합 함수 직접 구현
#import sys

read_ints = lambda: list(map(int, input().split())) 
read_int = lambda: read_ints()[0] #입력받은 리스트의 첫번째 원소 받기

def combination_recursive(seq, flag, N, M, idx):
    if idx==N: #인덱스 넘칠 경우
      if sum(flag)==M: #조합과 flag 합이 같다면
        for i,f in enumerate(flag):  #그때 flag 값이 참인 seq 원소를 출력
          if f==1:
            print(seq[i],end=' ')
        print()
      return

    flag[idx]=1
    combination_recursive(seq, flag, N, M, idx+1)
    flag[idx]=0
    combination_recursive(seq, flag, N, M, idx+1)

def combination_main(seq, M): 
  print("***combination***")
  N = len(seq) #리스트의 길이= N
  flag = [False] * N #해당 원소가 조합에 포함되는지 안되는지 체크하는 리스트 생성- 일단 다 false로 초기화
  combination_recursive(seq, flag, N, M, 0) #

def main():
  seq = read_ints()
  M = read_int() #조합의 크기
  combination_main(seq, M) #주어진 리스트에서 M개 뽑는 조합 함수 짜기

if __name__ == "__main__":
  main()