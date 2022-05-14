# 문제 : 최대공약수와 최소공배수
# 제출일 : 2022.05.14 (:)
'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
import math

a, b = list(map(int, input().split()))
print(math.gcd(a,b))
print(math.lcm(a,b))

# 모범 답안
#유클리드 호제법
def GCD(M, N): # 최대공약수
    if N == 0:
        return M
    return GCD(N,M%N)
M, N = map(int, input().split())
print(GCD(M, N))
#최소공배수
print(int(M*N/GCD(M,N)))