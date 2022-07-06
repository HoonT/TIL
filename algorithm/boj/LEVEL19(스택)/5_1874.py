# [TIL][Python] Boj - No.1874 (스택 수열)
## 제출일 : 2022.07.06 (16:00)
'''
스택 (stack)은 기본적인 자료구조 중 하나로, 
컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 
제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 
하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.
'''

## 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
push_list = []
result = []

for i in range(0,n):
    a = int(input())
    
    while cnt < a:
        cnt += 1
        push_list.append(cnt)
        result.append('+')
    
    if push_list[-1] == a:
        push_list.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print(*result, sep='\n')

## 피드백