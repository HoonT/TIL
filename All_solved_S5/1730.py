# [TIL][Python] Boj - No.1730 (판화)
## 제출일 : 2022.08.11 (19:00)
'''
W대학교 미술대학 조소과에서는 지루한 목판화 작업을 하는 학생들을 돕기 위해 판화 기계를 제작하였다.

기계는 로봇 팔이 쥔 조각도를 상하좌우 네 방향으로 움직일 수 있는 구조로서, 
조각도 아래에 목판을 놓으면 그 위에 선들을 자동으로 그어주는 기능을 가지고 있다.

목판에는 N2개의 점들이 일정한 간격으로 N행 N열의 격자모양을 이루며 찍혀있다. 
처음 로봇의 조각도를 올려놓는 위치는 항상 이 점들 중 맨 왼쪽 맨 위의 꼭짓점이다.

로봇 팔을 움직이는 명령의 순서가 주어졌을 때, 
목판 위에 패인 조각도의 혼적을 출력하는 프로그램을 작성하시오.

판화 기계는 작동 도중 로봇 팔이 격자 바깥으로 나가도록 하는 움직임 명령을 만나면, 
무시하고 그 다음 명령을 진행한다.
'''

## 내 풀이
n = int(input())
move = input()
draw = [['.' for _ in range(n)] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
pos = [0,0]

for i in range(len(move)):
    if move[i] == 'R':
        if pos[0] == n-1:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[2]
        pos[1] += dy[2]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
            
    elif move[i] == 'L':
        if pos[0] == 0:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[0]
        pos[1] += dy[0]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
            
    elif move[i] == 'U':
        if pos[1] == 0:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[3]
        pos[1] += dy[3]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
    else:
        if pos[1] == n-1:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[1]
        pos[1] += dy[1]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'

for i in range(n):
    print(''.join(draw[i]))

## 피드백