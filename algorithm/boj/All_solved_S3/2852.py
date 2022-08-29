# [TIL][Python] Boj - No.2852 (NBA 농구)
## 제출일 : 2022.08.29 (15:30)
'''
동혁이는 NBA 농구 경기를 즐겨 본다. 
동혁이는 골이 들어갈 때 마다 골이 들어간 시간과 팀을 적는 이상한 취미를 가지고 있다.

농구 경기는 정확히 48분동안 진행된다. 
각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램을 작성하시오.
'''

## 내 풀이
n = int(input())
end = 48*60
team1 = 0
team2 = 0
win = 0

for _ in range(n):
    team, goal = input().split()
    min, sec = map(int, goal.split(':'))
    time = min*60 + sec
    
    if team == '1':
        if win == 0:
            team1 += (end - time)
        win += 1
        if win == 0:
            team2 -= (end - time)
    else:
        if win == 0:
            team2 += (end - time)
        win -= 1
        if win == 0:
            team1 -= (end - time)
            
print('{:0>2}:{:0>2}'.format((team1)//60, (team1)%60))
print('{:0>2}:{:0>2}'.format((team2)//60, (team2)%60))

## 피드백