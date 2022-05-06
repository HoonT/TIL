# 문제 : 단어 정렬
# 제출일 : 2022.. (:)
'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
'''

# 내 풀이
a = int(input())
b = []
for i in range(a):
    b += [str(input())]
result = list(set(b))
result.sort()
result.sort(key=len)

print(*result, sep='\n')

# 모범 답안
