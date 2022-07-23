# [TIL][Python] Boj - No.1920 (수 찾기)
## 제출일 : 2022.07.23 (22:00)
'''
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
N = sorted(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))

## 피드백