# 문제 : 부녀회장이 될테야
'''
이 아파트에 거주를 하려면 조건이 있는데, 
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 
사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 
계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 
모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
'''

# 내 풀이
a = int(input())
a2 = []
a3 = []

for i in range(a):
    b = int(input())
    c = int(input())
    a1 = list(range(1,15))
    for n in range(b):        
        for i in range(1,c+1):
            a2 += [sum(a1[0:i])]
        a1.clear()
        a1 += a2
        a3 += [a2[i-1]]
        a2.clear()
    print(a3[-1])
# 모범 답안
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    people = [i for i in range(n + 1)]
    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]
    print(people[-1])