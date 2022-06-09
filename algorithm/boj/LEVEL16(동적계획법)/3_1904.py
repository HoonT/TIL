# 문제 : 01타일
# 제출일 : 2022.06.09 (20:30)
'''
N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다. 
(01, 10은 만들 수 없게 되었다.) 
또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.

우리의 목표는 N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것이다.
'''

# 내 풀이
a = int(input())

d = [0]*1000001
d[1] = 1
d[2] = 2
for i in range(3,a+1):
    d[i] = (d[i-1] + d[i-2]) % 15746

print(d[a])

# 작은 것에서 큰 것으로