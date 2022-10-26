import sys
from itertools import combinations
from copy import deepcopy as copy

read_ints = lambda: list(map(int, sys.stdin.readline().split()))
read_int = lambda: read_ints()[0]
sys.stdin = open("input.txt")

def find_dist(charge, house):
    result = 0
    for (i,j,dist) in house: #각 집에서 둘 중 더 가까운 충전소를 선택
        flag = 0
        if flag==2: return 999999
        min_dist = 99999
        for(x,y) in charge:
            if((abs(x-i) + abs(y-j))>dist):
                flag+=1
                continue
            else: min_dist = min(min_dist, (abs(x-i) + abs(y-j)))
        if flag==2: return 999999
        result+=min_dist
    return result

def main():
    house = []
    origin = []
    map = []
    nearest = 99999;
    for i in range(-15, 16):
            for j in range(-15, 16):
                origin.append((i,j)) # 충전소 올 수 있는 모든 좌표 저장

    t_num = read_int()
    for t in range(1, t_num+1):
        map = copy(origin)

        n = read_int()
        for i in range(n):
            x,y,dist = read_ints() #집의 좌표, 제한 거리 입력받기
            house.append((x,y,dist)) #집 정보 저장
            map.remove((x,y)) #집 좌표는 충전소 가능 좌표에서 제거

        for ch in combinations(map, 2): #충전소 좌표 2개 고르고, 집이랑 거리 계산
            charge = []
            for(x,y) in ch:
                charge.append((x,y))
                nearest = min(nearest, find_dist(charge,house)) #해당 충전소 좌표와 집과의 거리 조합 계산하고 최소 거리와 비교
                if nearest
        print(f"#{t} {nearest}")


if __name__ == "__main__":
    main()