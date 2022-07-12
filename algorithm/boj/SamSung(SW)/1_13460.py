# [TIL][Python] Boj - No.13460 (구슬 탈출 2)
## 제출일 : 2022.07.12 (13:00)
'''
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 
가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 
각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 
이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 
빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
'''

## 내 풀이
from sys import stdin
from collections import deque
input = stdin.readline

n, m = list(map(int, input().split()))
table = [list(input().strip()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = (-1,0,1,0)
dy = (0,1,0,-1)
deq = deque()

def start():
    rx, ry, bx, by = [0]*4
    for i in range(n):
        for j in range(m):
            if table[i][j] == 'R':
                rx, ry = i, j
            elif table[i][j] == 'B':
                bx, by = i, j
    deq.append((rx,ry,bx,by,0))
    check[rx][ry][bx][by] = True

def move(x, y, dx, dy, c):
    while table[x+dx][y+dy] != '#' and table[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c

def bfs():
    while deq:
        rx, ry, bx, by, d = deq.popleft()
        if d >= 10:
            break
        for i in range(4):
            _rx, _ry, r_cnt = move(rx, ry, dx[i], dy[i], 0)
            _bx, _by, b_cnt = move(bx, by, dx[i], dy[i], 0)
            if table[_bx][_by] == 'O':
                continue
            if table[_rx][_ry] == 'O':
                print(d+1)
                return
            if _rx == _bx and _ry == _by:
                if r_cnt > b_cnt:
                    _rx -= dx[i]
                    _ry -= dy[i]
                else:
                    _bx -= dx[i]
                    _by -= dy[i]
            if not check[_rx][_ry][_bx][_by]:
                check[_rx][_ry][_bx][_by] = True
                deq.append((_rx, _ry, _bx, _by, d+1))
    print(-1)
start()
bfs()

## 피드백