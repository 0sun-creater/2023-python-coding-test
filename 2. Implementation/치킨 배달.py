'''
[조건]
- 2 <= N <= 50, 1 <= M <= 13 (M은 폐업시키지 않을 치킨집을 선택할 개수)
- 0 : 빈칸 / 1 : 집 / 2 : 치킨집
- M <= 치킨집의 개수 <= 13
- "치킨 거리" : 집과 가장 가까운 치킨집 사이의 거리
- "도시의 치킨 거리" : 모든 집의 치킨 거리의 합
- 치킨 거리 != 도시의 치킨 거리
- "return 도시의 치킨 거리의 최솟값"👌

Flow✅
1. 먼저, 폐업시키지 않을 치킨집을 선택한다.(M부터 1까지 => 0까지가 아닌 이유는, 치킨집을 고르지 않으면 안되기 때문 and '1 <= M <= 13') => 조합으로 치킨집 선택?
2. (1)에서 구한 치킨집 들의 위치를 토대로, 각 집에서 최소 치킨거리를 찾는다.
3. (2)에서 구한 각 집에서의 최소 치킨 거리의 합이 도시의 치킨 거리보다 작으면, 도시의 치킨 거리의 값을 해당 값으로 업데이트한다.
4. 모든 조합을 순회할 때 까지 (1)로 돌아가 반복한다.
'''
import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split()) # n : 도시 크기, m : 선택할 치킨 집 개수

city = [] # 도시 정보
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split())) # 도시 정보 입력받기
    city.append(data)

chicken_pos = deque() # 모든 치킨 집 위치 저장하는 변수
for i in range(n):
    for j in range(n):
        if city[i][j] == 2: # 치킨집 : 2
            chicken_pos.append((i, j)) 

# comb : 모든 치킨 집의 위치에서 특정 개수만큼 치킨 집을 선택했을 때 만들 수 있는 조합
# x, y : 집의 위치
def get_min_dist(comb, x, y): # 특정 집에서 치킨 집으로부터 최소 거리 찾는 함수
    min_dist = float('inf') # 최소 거리
    for c_x, c_y in comb:
        min_dist = min(min_dist, abs(x - c_x) + abs(y - c_y))
    return min_dist 

count = m # 치킨 집을 몇 개 고를지(치킨 집 고르는 횟수)
total_min_dist = float('inf') # 도시의 치킨 거리 최솟값 저장하는 변수

while count != 0: # 치킨 집을 1개 이상은 무조건 고른다.
    
    chicken_comb = list(combinations(chicken_pos, count)) # 치킨 집 위치를 count개 선택한 조합 생성 => chicken_pos C count
    for comb in chicken_comb: # 조합을 하나씩 확인
        total_dist = 0 # 각 순회에서 도시의 치킨 거리
        for i in range(n): 
            for j in range(n):
                if city[i][j] == 1: # 위치가 집이라면
                    total_dist += get_min_dist(comb, i, j) # 최소 거리를 찾아서 더한다.
        total_min_dist = min(total_min_dist, total_dist) # 도시의 치킨 거리 최솟값을 업데이트한다.
    count -= 1 # 치킨 집을 고르는 횟수를 1 차감한다.

print(total_min_dist) # 출력