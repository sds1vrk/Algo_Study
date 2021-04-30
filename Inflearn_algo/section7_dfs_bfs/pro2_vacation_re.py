import sys
sys.stdin = open("input.txt", "rt")
def dfs(lev, s):
    global max_score
    if(lev > n):
        return
    if(n == lev):
        max_score = max(s, max_score)
    else:
        # 상담을 하고 다음 날짜로 이동
        dfs(lev+time[lev], s+score[lev])
        # 상담을 하지 않음
        dfs(lev+1, s)

if __name__ == "__main__":
    n = int(input())
    time = []
    score = []

    for i in range(n):
        a, b = map(int, input().split())

        time.append(a)
        score.append(b)
    max_score = -1
    dfs(0, 0)
    print(max_score)