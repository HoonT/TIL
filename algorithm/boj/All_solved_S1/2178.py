# [TIL][Python] Boj - No.2178 (미로 탐색)
## 제출일 : 2022.09.23 (15:30)
### 알고리즘 : Graph / DFS
'''
N×M크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 
(N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.

한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
'''

## 내 풀이
n, m = map(int, input().split())
line = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    line.append(list(input()))
queue = [[0, 0]]
line[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and line[x][y] == "1":
            queue.append([x, y])
            line[x][y] = line[a][b] + 1
print(line[n - 1][m - 1])

## 피드백