# [TIL][Python] Boj - No.1340 (연도 진행바)
## 제출일 : 2022.08.02 (17:30)
'''
문빙이는 새해를 좋아한다. 
하지만, 이제 새해는 너무 많이 남았다. 
그래도 문빙이는 새해를 기다릴 것이다.

어느 날 문빙이는 잠에서 깨면서 스스로에게 물었다. “잠깐, 새해가 얼마나 남은거지?”

이 문제에 답하기 위해서 문빙이는 간단한 어플리케이션을 만들기로 했다. 
연도 진행바라는 것인데, 이번 해가 얼마나 지났는지를 보여주는 것이다.

오늘 날짜가 주어진다. 이번 해가 몇% 지났는지 출력하는 프로그램을 작성하시오.
'''

## 내 풀이
month, day, year, time = input().split()
hour, min = map(int, time.split(':'))
year = int(year)
day = int(day[:-1])

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day_list = [31,28,31,30,31,30,31,31,30,31,30,31]

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    day_list[1] += 1

total_time = sum(day_list)*24*60
now_time = (sum(day_list[:month_list.index(month)]) + day-1)*24*60 + hour*60 + min

print((now_time/total_time)*100)

## 피드백