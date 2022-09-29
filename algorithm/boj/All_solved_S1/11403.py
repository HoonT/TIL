# [TIL][Python] Boj - No.11403 (경로 찾기)
## 제출일 : 2022.09.29 (16:00)
### 알고리즘 : Graph / Floyd Warshall
'''
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, 
i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
'''

## 내 풀이
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()

## 피드백