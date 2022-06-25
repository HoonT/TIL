# [TIL][Python] Boj - No.16139 (인간-컴퓨터 상호작용)
## 제출일 : 2022.06.25 (16:30)
'''
승재를 도와 특정 문자열 $S$, 
특정 알파벳 $\alpha$와 문자열의 구간 $[l,r]$이 주어지면 
$S$의 $l$번째 문자부터 $r$번째 문자 사이에 $\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 
승재는 문자열의 문자는 $0$번째부터 세며, $l$번째와 $r$번째 문자를 포함해서 생각한다. 
주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 $q$번 할 것이다.
'''

## 내 풀이
import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]
arr[0][ord(s[0])-97] = 1

for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1

for _ in range(int(input())):
    c,start,end = list(input().split())
    start,end = map(int,[start,end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])

## 피드백