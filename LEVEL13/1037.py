# 문제 : 약수
# 제출일 : 2022.. (:)
'''
양수 A가 N의 진짜 약수가 되려면, 
N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = list(map(int, input().split()))

b.sort()
if len(b) > 1:
    print(b[0]*b[len(b)-1])
elif len(b) == 1:
    print(b[0]**2)

# 모범 답안
