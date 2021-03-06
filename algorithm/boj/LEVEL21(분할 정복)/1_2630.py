# [TIL][Python] Boj - No.2630 (색종이 만들기)
## 제출일 : 2022.07.15 (15:00)
'''
아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 
각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 
주어진 종이를 일정한 규칙에 따라 잘라서
다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 
<그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 
나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 
모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 
이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 
하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 
잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

zero = 0
one = 0

def tree(x, y, n):
    global zero, one
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                tree(x, y, n//2)
                tree(x, y+n//2, n//2)
                tree(x+n//2, y, n//2)
                tree(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        zero += 1
    else:
        one += 1

tree(0,0,n)
print(zero)
print(one)

## 피드백