# [TIL][Python] Boj - No.11726 (2Xn 타일링)
## 제출일 : 2022.09.21 (16:00)
### 알고리즘 : DP
'''
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
n = int(input())
tile = [0, 1, 2]

for i in range(3, 1001):
  tile.append(tile[i-1] + tile[i-2])
print(tile[n] % 10007)

## 피드백