# 문제 : 그룹 단어 체커
'''
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
c = []
d = 0

for n in range(a):
    b = list(map(str, str(input())))
    for i in range(len(b)):
        if len(b) == 1:
            break
        else:
            if b[i] not in c:
                c += b[i]
                #print(c)

            elif b[i] in c:
                if b[i] == c[-1]:
                    c += b[i]
                    #print(c)

                elif b[i] != c[-1]:
                    d += 1
                    c.clear()
                    break       
            if i == len(b)-1:
                c.clear()
#print(c)
print(a-d)

# 모범 답안
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

    