# [TIL][Python] Boj - No.1331 (나이트 투어)
## 제출일 : 2022.08.01 (11:30)
'''
나이트 투어는 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며, 
마지막으로 방문하는 칸에서 시작점으로 돌아올 수 있는 경로이다. 

영식이는 6*6 체스판 위에서 또 다른 나이트 투어의 경로를 찾으려고 한다. 
체스판의 한 칸은 A, B, C, D, E, F 중에서 하나와 1, 2, 3, 4, 5, 6 중에서 
하나를 이어 붙인 것으로 나타낼 수 있다. 영식이의 나이트 투어 경로가 주어질 때, 
이것이 올바른 것이면 Valid, 올바르지 않으면 Invalid를 출력하는 프로그램을 작성하시오.
'''

## 내 풀이
from sys import stdin
input = stdin.readline

knight = [input() for _ in range(36)]
chess = [[0 for _ in range(6)] for _ in range(6)]
sx, sy = ord(knight[0][0]) - 65, int(knight[0][1]) - 1
chess[sx][sy] = 1

flag = True

if abs(ord(knight[0][0]) - ord(knight[-1][0])) == 2 and abs(int(knight[0][1]) - int(knight[-1][1])) == 1 \
            or abs(ord(knight[0][0]) - ord(knight[-1][0])) == 1 and abs(int(knight[0][1]) - int(knight[-1][1])) == 2:
    for i in range(1, len(knight)):
        nx, ny = ord(knight[i][0]) - 65, int(knight[i][1]) - 1
        if abs(nx - sx) == 2 and abs(ny - sy) == 1 or abs(nx - sx) == 1 and abs(ny - sy) == 2:
            chess[nx][ny] += 1
            if chess[nx][ny] != 1:
                flag = False
                break
        else:
            flag = False
            break
        sx, sy = nx, ny
else:
    flag = False

if flag:
    print("Valid")
else:
    print("Invalid")

## 피드백