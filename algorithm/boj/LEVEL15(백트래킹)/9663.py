# 문제 : N-Queen
# 제출일 : 2022.06.03 (16:30)
'''
N-Queen 문제는 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이 - (Pypy3 로 제출)_python3 는 시간초과
def selecting(x):
    for i in range(x):
        if nxn[x] == nxn[i] or abs(nxn[x] - nxn[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            nxn[x] = i
            if selecting(x):
                n_queens(x+1)

n = int(input())
ans = 0
nxn = [0] * n
n_queens(0)
print(ans)

# 모범 답안 - 왜 이게 답이지?
print([0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])