# [TIL][Python] Boj - No.1817 (짐 챙기는 숌)
## 제출일 : 2022.08.14 (15:30)
'''
숌은 짐을 챙겨서 겨울캠프에서 집으로 가려고 한다.
근데 숌은 공부를 많이 하러 캠프에 온 것이기 때문에 책을 엄청나게 많이 가지고 왔다. 
숌은 이 책을 방에 탑처럼 쌓아 놨다.

숌은 책을 박스에 차곡차곡 넣어서 택배로 미리 보내려고 한다.
책은 탑처럼 차곡차곡 쌓여있기 때문에, 차례대로 박스에 넣을 수밖에 없다.

각각의 책은 무게가 있다. 그리고 박스는 최대 넣을수 있는 무게가 있다. 
숌이 필요한 박스의 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''

## 내 풀이
N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    package = list(map(int, input().split()))
    cnt = 0
    weight = 0
    for i in range(N):
        if package[i] + weight > M:
            cnt += 1
            weight = 0
            weight += package[i]
        else:
            weight += package[i]

    print(cnt+1)

## 피드백