# 문제 : 정수 삼각형
# 제출일 : 2022.06.13 (13:30)
'''
맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
'''

# 내 풀이
amount = int(input()) # amount 보다 n으로 하자
triangle = [] # triangle 보다 t로 하자
for i in range(amount):
    triangle += [list(map(int, input().split()))]

for i in range(1,amount):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i])-1: # if i == j: 라고 하면 간편하다.
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[amount-1]))
