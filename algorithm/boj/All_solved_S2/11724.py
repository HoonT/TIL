# [TIL][Python] Boj - No.11724 (연결 요소의 개수)
## 제출일 : 2022.09.19 (14:30)
### 알고리즘 : Graph / DFS/BFS
'''
방향 없는 그래프가 주어졌을 때, 
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
sys.setrecursionlimit(10000)

def search(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            search(e)
            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        search(j)
        count += 1

print(count)

## 피드백