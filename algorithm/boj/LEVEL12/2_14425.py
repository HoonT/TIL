# 문제 : 문자열 집합
# 제출일 : 2022.05.20 (09:00)
'''
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 
집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a, b = list(map(int, input().split()))
list_n = []
list_m = []
result = 0
for i in range(a):
    list_n += [input()]
for j in range(b):
    list_m += [input()]
for i in range(b):
    if list_n.count(list_m[i]) != 0:
         result += 1

print(result)
# 모범 답안
pr = open(0).read().split('\n')
N, M = map(int, pr[0].split())
S = set()
for i in range(1,N+1):
    S.add(pr[i])
cnt = 0
for j in range(M):
    if pr[N+1+j] in S: cnt+=1
print(cnt)
