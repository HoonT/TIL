# 합
'''
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
'''

# 내풀이
n = int(input())
if n%2 == 1:
    print((n+1)*(n//2)+((n+1)//2))
elif n%2 == 0:
    print((n+1)*(n//2))

# 모범 답안
n = int(input())
print((n**2+n)//2)