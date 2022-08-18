# [TIL][Python] Boj - No.1707 (이분 그래프)
## 제출일 : 2022.08.18 (19:00)
'''
그래프의 정점의 집합을 둘로 분할하여, 
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 
이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
'''

## 내 풀이
from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

def search(graph, start):
    queue = deque()
    queue.append(start)
    if visit[start] == 0:
        visit[start] = 1 
    while queue:
        v = queue.popleft()

        color = visit[v]
        for i in graph[v]: 
            if visit[i] == 0:
                queue.append(i)
                if color == 1: 
                    visit[i] = 2
                else:
                    visit[i] = 1
            elif visit[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visit[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True

for i in range(k):
    flag = 0
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for j in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1, V + 1):
        if not search(graph, k):
            flag = 1
            break
    if flag == 0:
        print("YES")

## 피드백