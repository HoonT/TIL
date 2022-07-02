# [TIL][Python] Boj - No.13305 (주유소)
## 제출일 : 2022.07.02 (12:00)
'''
어떤 나라에 N개의 도시가 있다. 이 도시들은 일직선 도로 위에 있다. 
편의상 일직선을 수평 방향으로 두자. 
제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동하려고 한다. 

각 도시에 있는 주유소의 기름 가격과, 
각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 
제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.
'''

## 내 풀이
n = int(input())
way = list(map(int, input().split()))
oil = list(map(int, input().split()))

res = 0
m = oil[0]
for i in range(n-1):
    if oil[i] < m:
        m = oil[i]
    res += m * way[i]

print(res)

## 피드백