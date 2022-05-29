# 문제 : 숫자 카드
# 제출일 : 2022.05.18 (11:40)
'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 
아닌지를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))

result = [0*i for i in range(len(d))]
for i in range(len(d)):
    if b.count(d[i]) != 0:
        result[i] += 1

print(*result, sep=' ')

# 모범 답안
def solution():
    import sys
    _, A, _, B = sys.stdin.read().rstrip().split("\n")
    A = set(A.split())
    B = list(B.split())
    print(" ".join(map(lambda x: "1" if x in A else "0", B)))

solution()