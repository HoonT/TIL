# [TIL][Python] Boj - No.11279 (최대 힙)
## 제출일 : 2022.09.17 (15:00)
### 알고리즘 : Data Structure / Priority Queue
'''
널리 잘 알려진 자료구조 중 최대 힙이 있다. 
최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

## 내 풀이
import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)

## 피드백