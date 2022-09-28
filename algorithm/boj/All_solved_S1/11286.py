# [TIL][Python] Boj - No.11286 (절댓값 힙)
## 제출일 : 2022.09.28 (16:30)
### 알고리즘 : Data Structure / Priority Heap
'''
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

## 내 풀이
import sys
import heapq
input = sys.stdin.readline

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

## 피드백