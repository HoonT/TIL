# 기찍 N
'''
9개의 서로 다른 자연수가 주어질 때, 
이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = []
s = []
#s = a + list(map(int, input())) 은 틀렸다.

while len(s) != 9:
    a = s
    s = a + list(map(int, input().split()))
    if len(s) == 9:
        print(max(s))
        print(s.index(max(s)) + 1)
        break

# 모범 답안
l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)