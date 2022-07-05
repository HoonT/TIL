# [TIL][Python] Boj - No.4949 (균형잡힌 세상)
## 제출일 : 2022.07.05 (14:00)
'''
정민이의 임무는 어떤 문자열이 주어졌을 때, 
괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 
문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
'''

## 내 풀이
while True:
    a = input()
    if a == '.':
        break
    brackets = []
    judge = True
    for i in a:
        if i == '(' or i == '[':
            brackets.append(i)
        elif i == ')':
            if not brackets or brackets[-1] == '[':
                judge = False
                break
            elif brackets[-1] == '(':
                brackets.pop()
        elif i == ']':
            if not brackets or brackets[-1] == '(':
                judge = False
                break
            elif brackets[-1] == '[':
                brackets.pop()
    if judge == True and not brackets:
        print('yes')
    else:
        print('no')

## 피드백