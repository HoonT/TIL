# [TIL][Python] Boj - No.10845 (큐)
## 제출일 : 2022.08.26 (15:30)
'''
정수를 저장하는 큐를 구현한 다음, 
입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

## 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
que = []

for _ in range(n):
    a = input().split()
    if a[0] == 'push':
        que.append(a[1])
    elif a[0] == 'pop':
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif a[0] == 'size':
            print(len(que))
    elif a[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)

## 피드백