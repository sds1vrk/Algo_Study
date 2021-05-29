# 플로이드 와샬 문제

def solution(n, costs):


    dis = [[5000] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dis[i][i] = 0

    for i in costs:
        a, b, c = i[0],i[1],i[2]
        dis[a][b] = c


    answer=0

    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])


    for k in dis[0]:
        if k!=5000:
            answer+=k

    print(dis)

    return answer




solution(4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])