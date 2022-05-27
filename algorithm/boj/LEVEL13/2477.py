# 문제 : 참외밭
# 제출일 : 2022.05.27 (09:00)
'''
1m2의 넓이에 자라는 참외의 개수와, 
참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 
반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다. 
이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
melon = int(input())
values = [input().split() for _ in range(6)] 
directions = [int(v[0]) for v in values]
lengths = [int(v[1]) for v in values] 
max_lengths, box_lengths = [], []

for i in range(1, 5):
    if directions.count(i) == 1:
        max_lengths.append(lengths[directions.index(i)]) 
        temp = directions.index(i) + 3
        if temp >= 6:
            temp -= 6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)

# 모범 답안
k = int(input())
arr = list()
for _ in range(6):
    arr.append(list(map(int, input().split())))
arr *= 2
repeat = -1
for i in range(6):
    if arr[i][0] == arr[i+2][0] and arr[i+1][0] == arr[i+3][0]:
        repeat = i
        break
size = (arr[i][1]+arr[i+2][1])*(arr[i+1][1]+arr[i+3][1])-(arr[i+1][1])*(arr[i+2][1])
print(size*k)
