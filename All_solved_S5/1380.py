# [TIL][Python] Boj - No.1380 (귀걸이)
## 제출일 : 2022.08.04 (12:00)
'''
파스칼 고등학교에 다니는 많은 여학생들은 규정에 없는 귀걸이를 착용한 채 도망다닙니다. 
Sneddon 교감선생님은 흔들거리는 긴 빨간 귀걸이들을 볼때마다 압수합니다.

교감선생님은 귀걸이를 압수당한 여학생들을 숫자를 매겨 리스트를 작성하고 있습니다. 
그리고 압수한 귀걸이 뒤쪽에 여학생 번호와 마음대로 선택한 'A' 또는 'B'를 함께 적어두었습니다.

모든 정규 일과와 방과후 수업의 감금이 끝나면, 
여학생들은 교감선생님을 찾아와 귀걸이를 돌려받습니다. 
불행하게도 어느 날, 교감선생님은 귀걸이가 든 봉투를 잃어버렸고, 
하나를 끝내 찾지 못했습니다.

귀걸이를 받지 못해 화난 소녀의 이름을 교감선생님께 알려주세요.
'''

## 내 풀이
n = int(input())
result = []
cnt = 1

while n != 0:
    name_list = []
    num_list = []
    for i in range(n):
        name_list.append(input())
    for i in range(2*n-1):
        num, label = input().split()
        num = int(num)
        if num in num_list:
            num_list.remove(num)
        else:
            num_list.append(num)
    print(cnt, name_list[num_list.pop()-1])
    cnt += 1
    n = int(input())

## 피드백