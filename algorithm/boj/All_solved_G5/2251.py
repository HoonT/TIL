# [TIL][Python] Boj - No.2251 (물통)
## 제출일 : 2022.08.17 (20:00)
'''
각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 
처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다. 

이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 
이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다. 
이 과정에서 손실되는 물은 없다고 가정한다.

이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다. 

첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 
물의 양을 모두 구해내는 프로그램을 작성하시오.
'''

## 내 풀이
from collections import deque

a,b,c = map(int, input().split())
q = deque()
q.append((0,0))

visit = [[False]*(b+1) for _ in range(a+1)]
visit[0][0] = True

result = []

def select(x,y):
    if not visit[x][y]:
        visit[x][y] = True
        q.append((x,y))

def search():
    while q:
        x, y = q.popleft()
        z = c-(x+y)
        if x == 0:
            result.append(z)
        
        move = min(x, b-y)
        select(x-move, y+move)
        
        move = min(x, c-z)
        select(x-move, y)
        
        move = min(y, a-x)
        select(x+move, y-move)
        
        move = min(y, c-z)
        select(x,y-move)
        
        move = min(z, a-x)
        select(x+move, y)
        
        move = min(z, b-y)
        select(x, y+move)

search()
result.sort()
print(*result)

## 피드백