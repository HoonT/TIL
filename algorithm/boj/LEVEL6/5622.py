# 문제 : 다이얼
'''
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
할머니가 외운 단어가 주어졌을 때, 
이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = str(input())
b = list(map(str, str(a)))
c = []

for i in range(len(b)):
    if 65 <= ord(b[i]) < 83:
        c += [((ord(b[i])-59)//3)]
    elif ord(b[i]) == 83:
        c += [7]         
    elif 84 <= ord(b[i]) <= 86:
        c += [8]
    elif 87 <= ord(b[i]):
        c += [9]
    
print(sum(c)+len(c))

# 모범 답안
print(sum((ord(i)-62-(i in 'SVYZ')-(i=='Z'))//3+2 for i in input()))