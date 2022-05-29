# 문제 : 대칭 차집합
# 제출일 : 2022.05.27 (08:00)
'''
자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 
이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
num_a, num_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(set(a)-set(b))
d = list(set(b)-set(a))
print(len(c)+len(d))

# 모범 답안
input()
a = list(input().split())
b = list(input().split())
print(2*len(set(a+b)) - (len(a)+len(b)))