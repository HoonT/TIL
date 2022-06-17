# [TIL][Python] Boj - No.2156 (포도주 시식)
# 제출일 : 2022.06.17 (13:00)
'''
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 
마신 후에는 원래 위치에 다시 놓아야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.
'''

## 내 풀이
n = int(input())

b = [0]
for i in range(n):
    b.append(int(input()))

if n == 1:
    print(b[1])
else:
    c = [0]*(n+1)
    c[1] = b[1]
    c[2] = b[1] + b[2]
    
    for i in range(3, n+1):
        c[i] = max(c[i-1], b[i] + b[i-1] + c[i-3], b[i] + c[i-2]) # 수정 후
        # 수정 전 c[i] = max(b[i] + b[i-1] + c[i-3], b[i] + c[i-2])
    
    print(c[n])

## 피드백