# 문제 : 하노이 탑 이동 순서
# 제출일 : 2022.04.29 (22:00)
'''
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라.
'''

# 내 풀이
def move(N, start, to):
    print('{} {}'.format(start, to))


def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

a = int(input())
print(2**a-1)     
hanoi(a, '1', '3', '2')