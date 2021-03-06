# 문제 : 스도쿠
# 제출일 : 2022.06.04 (14:00)
'''
게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 
모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)

# 모범 답안
board = [list(input()) for _ in range(9)]

def cross(A, B):
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def grid_values(board):
    chars = []
    for l in board:
        temp = [c for c in l if c in digits or c in '0.']
        chars += temp
    return dict(zip(squares, chars))

def parse_grid(board):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(board).items():
        if d in digits and not assign(values, s, d):
            return False
    return values
    
def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values):
    width = 1+max(len(values[s]) for s in squares)
    for r in rows:
        print(' '.join(values[r+c] for c in cols))

def solve(board): return search(parse_grid(board))

def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s]) 

def some(seq):
    for e in seq:
        if e: return e
    return False

display(solve(board))