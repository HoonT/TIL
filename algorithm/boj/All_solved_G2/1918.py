# [TIL][Python] Boj - No.1918 (후위 표기식)
## 제출일 : 2022.11.15 (14:30)
### 알고리즘 : Data Structure / Stack
'''
수식은 일반적으로 3가지 표기법으로 표현할 수 있다. 
연산자가 피연산자 가운데 위치하는 중위 표기법(일반적으로 우리가 쓰는 방법이다), 
연산자가 피연산자 앞에 위치하는 전위 표기법(prefix notation), 
연산자가 피연산자 뒤에 위치하는 후위 표기법(postfix notation)이 그것이다. 
예를 들어 중위 표기법으로 표현된 a+b는 전위 표기법으로는 +ab이고, 후위 표기법으로는 ab+가 된다.

이 문제에서 우리가 다룰 표기법은 후위 표기법이다. 
후위 표기법은 위에서 말한 법과 같이 연산자가 피연산자 뒤에 위치하는 방법이다. 
이 방법의 장점은 다음과 같다. 
우리가 흔히 쓰는 중위 표기식 같은 경우에는 덧셈과 곱셈의 우선순위에 차이가 있어 왼쪽부터 차례로 계산할 수 없지만 
후위 표기식을 사용하면 순서를 적절히 조절하여 순서를 정해줄 수 있다. 또한 같은 방법으로 괄호 등도 필요 없게 된다. 
예를 들어 a+b*c를 후위 표기식으로 바꾸면 abc*+가 된다.

중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다. 
우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다. 
그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다. 
그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다.
마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

이러한 사실을 알고 중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오
'''

## 내 풀이
line = list(input())
stack = []
ans = ''

for letter in line:
    if letter.isalpha():
        ans += letter
    else:
        if letter == '(':
            stack.append(letter)
        elif letter == '*' or letter == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                ans += stack.pop()
            stack.append(letter)
        elif letter == '+' or letter == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(letter)
        elif letter == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack :
    ans +=stack.pop()
print(ans)

## 피드백