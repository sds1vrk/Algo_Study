import sys
sys.stdin=open("input.txt","r")


def dfs(v):
    # 종료 조건부터 무조건 걸기
    if v>7:
        return

    else :
        # 전위 순회 : 본연의 일을 하고 ==> 왼쪽, 오른쪽 호출이 넘어감
        print(v,end=" ")
        dfs(v*2)
        dfs(v*2+1)


        # 중위 순회 : 왼쪽 먼저 처리하고 ==> 자기 일을 , 그리고 부모일을 처리함
        dfs(v*2)
        print(v,end=" ")
        dfs(v*2+1)

        # 후위 순회 : 왼쪽 오른쪽 다 처리하고 자기 본연의 일을 함
        # 대표적인 예, 병합정렬, 왼쪽일, 오른쪽일을 다 처리하고 본연의 일을 처리
        dfs(v * 2)
        dfs(v * 2 + 1)
        print(v, end=" ")


n=int(input())
dfs(1)