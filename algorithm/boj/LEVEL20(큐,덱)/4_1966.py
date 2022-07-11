# [TIL][Python] Boj - No.1966 (프린터 큐)
## 제출일 : 2022.07.11 (14:00)
'''
하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 
이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 
중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
'''

## 내 풀이
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, m = list(map(int, input().split()))
    li = list(map(int, input().split()))
    table = [0 for i in range(n)]
    table[m] = 1
    cnt = 0
    while True:
        if li[0] == max(li):
            cnt += 1
            if table[0] == 1:
                print(cnt)
                break
            else:
                del li[0]
                del table[0]
        else:
            li.append(li[0])
            del li[0]
            table.append(table[0])
            del table[0]

## 피드백