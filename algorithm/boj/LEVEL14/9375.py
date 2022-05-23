# 문제 : 패션왕 신해빈
# 제출일 : 2022.05.23 (14:00)
'''
해빈이가 가진 의상들이 주어졌을때 과연 
해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
'''

# 내 풀이
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c = {}
    count = {}
    for _ in range(int(input())):
        a1, b1 = input().split()
        c[a1] = b1
    for i in c.values():
        try: count[i] += 1
        except: count[i] = 1
    ans = 1
    for j in count.values():
        ans *= j+1
    print(ans-1)
    c.clear()
    count.clear()

# 모범 답안
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    
    wear = []
    for i in range(n):
        wear.append(input().split()[1])
        
    set_wear = tuple(set(wear))
    
    gear = []
    for i in range(len(set_wear)):
        gear.append(wear.count(set_wear[i]))
        
    result = 1
    for t in gear:
        result *= (t + 1)
    
    print(result - 1)