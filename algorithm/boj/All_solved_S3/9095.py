# [TIL][Python] Boj - No.9095 (1,2,3 더하기)
## 제출일 : 2022.09.16 (18:00)
### 알고리즘 : DP
'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
case = int(input())  
        
def search(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return search(n-1) + search(n-2) + search(n-3)

for _ in range(case):
    n = int(input())
    print(search(n))

## 피드백