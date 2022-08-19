# [TIL][Python] Boj - No.2573 (빙산)
## 제출일 : 2022.08.19 (16:00)
'''
빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 
배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 
동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 
바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 

한 덩어리의 빙산이 주어질 때, 
이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 
그림 1의 빙산에 대해서는 2가 답이다. 
만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.
'''

## 내 풀이
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split())))
new = [[0 for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def attach(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if ice[x][y] > 0:
        ice[x][y] = 0
        attach(x-1,y)
        attach(x+1,y)
        attach(x,y-1)
        attach(x,y+1)
        return True
    return False

ans = 0

while True:
    cnt_0 = 0
    
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                        continue
                    if ice[nx][ny] == 0:
                        cnt += 1
                if ice[i][j] - cnt <= 0:
                    new[i][j] = 0
                else:
                    new[i][j] = ice[i][j] - cnt
            else:
                cnt_0 += 1
    if cnt_0 == n*m:
        print(0)
        break
    result = 0
    for i in range(n):
        for j in range(m):
            if attach(i,j) == True:
                result += 1
    if result >= 2:
        print(ans)
        break
    ans += 1
    
    ice = new
    new = [[0 for _ in range(m)] for _ in range(n)]

## 피드백