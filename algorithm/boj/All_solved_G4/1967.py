# [TIL][Python] Boj - No.1967 (트리의 지름)
## 제출일 : 2022.11.28 (15:30)
### 알고리즘 : Graph / Tree / DFS
'''
트리(tree)는 사이클이 없는 무방향 그래프이다. 
트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 
정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 
트리의 지름을 구해서 출력하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

def dfs(x, plus):
    for i in tree[x]:
        a,b = i
        if dis[a] == -1:
            dis[a] = plus + b
            dfs(a, plus+b)
    
for _ in range(n-1):
    start, end, len = map(int, input().split())
    tree[start].append([end, len])
    tree[end].append([start,len])

dis = [-1]*(n+1)
dis[1] = 0
dfs(1,0)

start = dis.index(max(dis))
dis = [-1]*(n+1)
dis[start] = 0
dfs(start,0)

print(max(dis))

## 피드백