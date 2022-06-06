# 문제 : 스타트와 링크
# 제출일 : 2022.06.06 (13:00)
'''
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, 
i번 사람과 j번 사람이 같은 팀에 속했을 때, 
팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.
'''

# 내 풀이 - 시간초과
def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)

# 모범 답안
import sys
input = sys.stdin.readline

def cal_diff(team_list: list) -> None: 
    another_team_list = list(set(range(N)) - set(team_list))
    team_sum = 0
    for i, v in enumerate(team_list[:-1]):
        for v2 in team_list[i+1:]:
            team_sum += ability[v][v2] + ability[v2][v]
    
    another_team_sum = 0
    for i, v in enumerate(another_team_list[:-1]):
        for v2 in another_team_list[i+1:]:
            another_team_sum += ability[v][v2] + ability[v2][v]
    
    ans.append(abs(team_sum - another_team_sum))

    return None


def dfs(team_list: list) -> None:
    if len(team_list) == N/2:
        cal_diff(team_list)
        return None
    
    for i in range(team_list[-1] if team_list else 0, N):
        if team_list and team_list[0] != 0:
          return None
        if i not in team_list:
            team_list.append(i)
            dfs(team_list)
            team_list.pop()

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
ans = []
dfs([])
print(min(ans))