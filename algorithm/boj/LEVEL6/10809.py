# 문제 : 알파벳 찾기
'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
input1 = str(input())
output1 = list(map(str, str(input1)))


for i in range(97, 123):
    if chr(i) in output1:
        print(output1.index(chr(i)))
    else:
        print(-1)
        
# 모범 답안
print(*map(input().find,map(chr,range(97,123))))