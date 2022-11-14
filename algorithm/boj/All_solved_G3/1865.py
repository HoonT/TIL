# [TIL][Python] Boj - No.1865 (웜홀)
## 제출일 : 2022.11.14 (18:00)
### 알고리즘 : Graph / Bellman-Ford
'''
월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다. 
(단 도로는 방향이 없으며 웜홀은 방향이 있다.) 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 
특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다. 
웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다. 
한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 
출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다. 

여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.
'''

## 내 풀이
import sys
input = sys.stdin.readline
inf = int(1e9)

def bf(start):
    dist = [inf for i in range(n + 1)]
    dist[start] = 0
    
    for i in range(n):
        
        for road in roads:
            go = road[0]
            arrive = road[1]
            time = road[2]

            if dist[arrive] > time + dist[go]:
                dist[arrive] = time + dist[go]
                if i == n-1:
                    return True
    return False
        
case = int(input())
for _ in range(case):
    n,m,w = map(int, input().split())
    roads = []
    for i in range(m):
        s,e,t = map(int, input().split())
        roads.append((s,e,t))
        roads.append((e,s,t))
    for i in range(w):
        s,e,t = map(int, input().split())
        roads.append((s,e,-t))

    ans = bf(1)
    if ans:
        print('YES')
    else:
        print('NO')

## 피드백