# 이 문제의 핵심은 간선을 저장하는 데 있다.
# 갔던 길이를 또 저장하지 않기 위해 set을 이용

def solution(dirs):


    # (행,열)
    # (0,-1)   (0,0) (0,1) (0,2)
    # ()   (1,0) (1,1) (1,2)
    #   (2,0) (2,1) (2,2)

    start = [5, 5]

    # 방문 여부 체크를 할때 전체 좌표를 기록할까?
    # 너무 비효율적, 마지막 도착 지점 구한다음에 뺴는게 거리르 뺴는게 나을것같음
    # 최종 (3,0) (5,5)둘 사이에 거리는
    # (5-3) + (5-0) ==> 2+5 ==> 7



    # U,D,R,L
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # visit[x,y]=0
    # [[x,y],[x,y],[x,y]]
    # visit = [[0] * 11 for _ in range(11)]
    visit=set()

    # print(visit)

    x, y = start[0], start[1]
    # visit[x][y] = 1
    cnt = 0

    for i in dirs:
        # x=start[0]
        # y=start[1]

        if i == "U":
            nx = x + dx[0]
            ny = y + dy[0]

        elif i == "D":
            nx = x + dx[1]
            ny = y + dy[1]

        elif i == "R":
            nx = x + dx[2]
            ny = y + dy[2]

        else:
            nx = x + dx[3]
            ny = y + dy[3]
        # (행,열) (nx,ny)
        if ny < 0 or ny > 10 or nx < 0 or nx > 10:
            continue

        if (x,y,nx,ny) not in visit:
            visit.add((x,y,nx,ny))
            visit.add((nx,ny,x,y))
            cnt += 1

        x = nx
        y = ny

    print(visit)
    # 최종 (3,0) (5,5)둘 사이에 거리는
    # (5-3) + (5-0) ==> 2+5 ==> 7
    # (3,4), (5,5) ==> 5-3 +

    print(cnt)
    # print(x,y)
    # k=(5-x)+(5-y)
    # print(k)
    return cnt

solution("ULURRDLLU")