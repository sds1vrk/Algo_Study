
# 문제 해결 :
# 재귀 함수를 이용한 풀이
# 사이즈가 1이 될때까지 재귀 호출
# 만약 1이면 멈추고 0 or 1의 개수 세기
# 1이 아니면 주어진 배열의 사이즈 전체가 0인지 1인지 확인
# - 0 or 1이라면 o or 1 Count 하기
# 아니라면 size를 2로 줄이고 다시 4개에 대해 재귀함수 호출
# 인자는 시작점 (x,y)를 넘겨준다.
# (0,0)  x,y // (0,2)  x,y+len(size)==> (2,0)  x+len(size), 0 // (2,2)  x+len(size), y+len(size)


def solution(arr):

    size=len(arr)

    def pan(x,y,size):
        temp=arr[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if temp!=arr[i][j]:
                    return False
        return True


    def dfs(x,y,size):

        global zero_count
        global one_count

        if size==1:
            if arr[x][y]==1:
                one_count+=1
            else :
                zero_count+=1

        else :
            # 주어진 배열의 사이즈 전체가 0인지 1인지 확인
            flag=pan(x,y,size)

            if flag:
                # print("flag")
                # 주어진 전체 배열이 0 or 1이기 때문에 어떤것인지 체크하기
                tem=arr[x][y]
                if tem==1:
                    one_count += 1

                else :
                    zero_count+=1


            else :
                # 4방향에 대해 다시 재귀
                size=size//2
                # (0,0)  a,b // (0,2)  a,b+len(size) // (2,0)  a+len(size), 0 // (2,2)  a+len(size), b+len(size)
                dfs(x,y,size)
                dfs(x,y+size,size)
                dfs(x+size,y,size)
                dfs(x+size,y+size,size)


    dfs(0,0,size)

    print(zero_count,one_count)

    answer = [zero_count,one_count]
    return answer

zero_count=0
one_count=0


solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])