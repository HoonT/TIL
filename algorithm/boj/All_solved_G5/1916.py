# [TIL][Python] Boj - No.1916 (최소비용 구하기)
## 제출일 : 2022.08.25 (17:00)
'''
N개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 

우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 

A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 
도시의 번호는 1부터 N까지이다.
'''

## 내 풀이
from heapq import heappush, heappop
import sys

inf = 10e8
city = int(input())
bus = int(input())
cost_map = [[] for _ in range(city + 1)]
table = [inf for _ in range(city + 1)]

for _ in range(bus):
    s, e, c = map(int, input().split())
    cost_map[s].append([c, e])
start, end = map(int, input().split())

def dijkstra(start):
    table[start] = 0
    heap = []
    heappush(heap, [0, start])
    
    while heap:
        d, x = heappop(heap)
        
        if table[x] < d:
            continue
        
        for nw, nx in cost_map[x]:
            nd = d + nw
            
            if table[nx] > nd:
                heappush(heap, (nd, nx))
                table[nx] = nd

dijkstra(start)
print(table[end])

## 피드백