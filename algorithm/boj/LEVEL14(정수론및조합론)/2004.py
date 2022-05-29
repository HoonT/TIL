# 문제 : 조합 0의 개수
# 제출일 : 2022.05.25 (09:00)
'''
math.comb(n,m)의 끝자리 0의 개수를 출력하는
프로그램을 작성하시오.
'''

# 내 풀이
n, m = map(int, input().split())

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))

# 모범 답안
g=lambda n,k:sum(n//k**i for i in range(1,31));n,m=map(int,input().split());l=n-m;h=lambda k:g(n,k)-g(m,k)-g(l,k);print(min(h(2),h(5)))