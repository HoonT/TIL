# [TIL][Python] Boj - No.10816 (숫자 카드 2)
## 제출일 : 2022.07.24 (14:00)
'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 

정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
from collections import Counter
def sol():
    N = int(sys.stdin.readline())
    cards = sorted(Counter(map(int, sys.stdin.readline().split(" "))).items(), key= lambda x: x[0])
    N = len(cards)
    M = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    
    answer = []
    for number in numbers:
        left = 0
        right = N-1
        middle = int((left+right)/2)
    
        while left < right:
            if number == cards[middle][0]:
                break
            elif number > cards[middle][0]:
                left = middle + 1
            else:
                right = middle - 1
            middle = int((left+right)/2)
        
        if number == cards[middle][0]:
            answer.append(cards[middle][1])
        else:
            answer.append(0)
        
    print(' '.join(map(str,answer)))

sol()

## 피드백