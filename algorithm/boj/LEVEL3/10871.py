# X보다 작은 수
'''
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
n, x = map(int, input().split())
a = list(map(int, input().split()))
n = len(a)

for i in a:
    if i < x:
        print(i, end=' ')

# 모범 답안
a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))