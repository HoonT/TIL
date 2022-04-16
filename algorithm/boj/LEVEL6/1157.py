# 문제 : 단어 공부
'''
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
'''

# 내 풀이
a = str(input())

def flatten(list):
    result = []
    for item in list:
        result.extend(item)
    return result

b = flatten(a)
c = []
for i in range(len(b)):
    if 97 <= ord(b[i-1]) < 123:
        c += chr(ord(b[i-1])-32)
    else:
        c += chr(ord(b[i-1]))

d = []
for n in range(65, 91):
    d += [c.count(chr(n))]

if len(d) == 1:
    print(chr(c[0])+65)
else:    
    if d.count(max(d)) >= 2:
        print('?')
    elif d.count(max(d)) == 1:
        print(chr(d.index(max(d))+65))
        
# 모범 답안
n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
  result.append(n.count(i))
if result.count(max(result)) > 1:
  print("?")
else:
  print(alpa[result.index(max(result))])