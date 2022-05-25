# 문제 : 듣보잡
# 제출일 : 2022.. (:)
'''
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a, b = map(int, input().split())
list1 = []
list2 = []

for i in range(a):
    list1 += [input()]
for j in range(b):
    list2 += [input()]

nonlist = list(set(list1)&set(list2))
nonlist.sort()
print(len(nonlist))
print(*nonlist, sep='\n')

# 모범 답안
n,m,*l=open(0).read().split()
n=int(n)
s=sorted(set(l[:n])&set(l[n:]))
print(len(s),*s,sep='\n')