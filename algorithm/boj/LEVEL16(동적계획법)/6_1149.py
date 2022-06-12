# 문제 : RGB거리
# 제출일 : 2022.06.12 (15:30)
'''
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
3. i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

# 내 풀이
house = int(input())
color = []
for i in range(house):
    color.append(list(map(int, input().split())))

for j in range(1, len(color)):
    color[j][0] = min(color[j-1][1], color[j-1][2]) + color[j][0]
    color[j][1] = min(color[j-1][0], color[j-1][2]) + color[j][1]
    color[j][2] = min(color[j-1][1], color[j-1][0]) + color[j][2]
    
print(min(color[house-1][0],color[house-1][1],color[house-1][2]))

# 시작점이 3가지이므로 3가지의 경우를 구하고 각 경우의 수의 최솟값을 구해준다
