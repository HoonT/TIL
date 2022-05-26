# 문제 : 서로 다른 부분 문자열의 개수
# 제출일 : 2022.05.27 (08:30)
'''
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
string = str(input())
strings = []

for i in range(len(string)):
    for j in range(len(string) - i):
        strings.append(string[j:j+i+1])
        
print(len(set(strings)))

# 모범 답안
A=input()
print(sum([len(set([A[i:i+l] for i in range(len(A)-l+1)])) for l in range(1,len(A)+1)]))