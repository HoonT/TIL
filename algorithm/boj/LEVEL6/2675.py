# 문제 :
'''
문자열 S를 입력받은 후에, 
각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
'''

# 내 풀이
T = int(input())
for i in range(1,T+1):
    s = list(map(str,input().strip()))
    s.remove(' ')
    r = int(s[0])

    for j in range(1,len(s)):
        print(s[j]*r, end='')
    print()

# 모범 답안
# X
