# 문제 : 나이순 정렬
# 제출일 : 2022.05.10 (15:30)
'''
이때, 회원들을 나이가 증가하는 순으로, 
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
input= sys.stdin.readline

N= int(input().rstrip())
lst=[]
for i in range(N):
    lst.append(list(input().split()))
    lst[i][0] = int(lst[i][0])

lst.sort(key=lambda x:x[0])

for i in lst:
    print(i[0],i[1])

# 모범 답안
from sys import stdin, stdout

users_by_age = [[] for _ in range(200+1)]

for line in stdin.read().splitlines(True)[1:]:
    users_by_age[int(line.split()[0])].append(line)

stdout.write(''.join(
    ''.join(u)
    for u in
    users_by_age
))