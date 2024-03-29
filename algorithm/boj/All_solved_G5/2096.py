# [TIL][Python] Boj - No.2096 (내려가기)
## 제출일 : 2022.09.02 (14:30)
'''
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 
내려가기 게임을 하고 있는데, 
이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 
그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 
바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다.

별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 
빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때,
얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 
점수는 원룡이가 위치한 곳의 수의 합이다.
'''

## 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
max_first = [0] * 3
min_first = [0] * 3

max_second = [0] * 3
min_second = [0] * 3

for _ in range(n):
    a, b, c = map(int, input().split())
    
    for i in range(3):
        if i == 0:
            max_second[i] = a + max(max_first[i], max_first[i+1])
            min_second[i] = a + min(min_first[i], min_first[i+1])
        elif i == 1:
            max_second[i] = b + max(max_first[i-1], max_first[i], max_first[i+1])
            min_second[i] = b + min(min_first[i-1], min_first[i], min_first[i+1])
        else:
            max_second[i] = c + max(max_first[i], max_first[i-1])
            min_second[i] = c + min(min_first[i], min_first[i-1])
    
    for j in range(3):
        max_first[j] = max_second[j]
        min_first[j] = min_second[j]

print(max(max_first), min(min_first))

## 피드백