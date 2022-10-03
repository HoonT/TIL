# [TIL][Python] Boj - No.1167 (트리의 지름)
## 제출일 : 2022.10.03 (16:00)
### 알고리즘 : Graph / DFS / Tree
'''
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 

트리의 지름을 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

case = int(input())
tree = [[] for _ in range(case+1)]

for _ in range(case):
    a = list(map(int, input().split()))
    for i in range(1,len(a)-1,2):
        tree[a[0]].append([a[i],a[i+1]])

def dfs(start, visit):
    for a,b in tree[start]:
        if visit[a] == -1:
            visit[a] = visit[start]+b
            dfs(a,visit)

visit1 = [-1] * (case+1)
visit1[1] = 0
dfs(1,visit1)

start = visit1.index(max(visit1))
visit2 = [-1] * (case+1)
visit2[start] = 0
dfs(start,visit2)

print(max(visit2))

## 피드백