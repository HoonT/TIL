# [TIL][Python] Boj - No.2110 (공유기 설치)
## 제출일 : 2022.08.23 (15:00)
'''
도현이의 집 N개가 수직선 위에 있다. 
각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 
가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline

# input setting
n, m = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

# binary setting - distance
start = 1
end = home[-1] - home[0]
result = 0

# binary search
if m == 2:
    print(end)
else:
    while start < end:
        mid = (start + end) // 2
        pin = home[0]
        cnt = 1
        
        for i in range(n):
            if (home[i] - pin) >= mid:
                cnt += 1
                pin = home[i]
        if cnt >= m:
            result = mid
            start = mid + 1
        elif cnt < m:
            end = mid
    print(result)

## 피드백