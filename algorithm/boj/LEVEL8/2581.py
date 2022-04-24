# 문제 : 소수
'''
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
'''

# 내 풀이 (핵심 : 1은 소수가 아니다.)
a = int(input())
b = int(input())
c = []
d = list(range(a,b+1)) 

if a != b:
    for i in range(a,b+1):
        for n in range(2,i):
            if i%n == 0:
                c += [i]
                break
    if len(list(set(d)-set(c))) >= 1:
        if 1 in list(set(d)-set(c)):
            e = list(set(d)-set(c)-set([1]))
            print(sum(e))
            print(min(e))
        else:
            print(sum(list(set(d)-set(c))))
            print(min(list(set(d)-set(c))))
    else:
        print(-1)
elif a == b:
    if a == 1:
        print(-1)
    else:
        for n in range(2,a):
            if a%n == 0:
                c += [a]
                break
        if len(c) >= 1:
            print(-1)
        else:
            print(a)
            print(a)
            
# 모범 답안
arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

m = int(input())
n = int(input())
nums = [i for i in range(m, n+1) if arr[i]]
print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')
