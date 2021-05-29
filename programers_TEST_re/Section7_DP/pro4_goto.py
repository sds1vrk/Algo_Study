def solution(m, n, puddles):
    # n,m=m,n
    # n이 행, m이 열
    a = [[0 * i for i in range(m)] for _ in range(n)]

    # print(a)

    for i in range(len(puddles)):
        # x,y=puddles[i][0],puddles[i][1]
        x,y=puddles[i]
        a[y-1][x-1]=-1

    print(a)

    answer = 0
    return answer


solution(4,3,[[2, 2]])