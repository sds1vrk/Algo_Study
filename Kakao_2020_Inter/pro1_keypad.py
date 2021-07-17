# 키패드 누르기

# 왼속 시작 위차 *, 오른쪽 시작 위치 #
# 왼쪽은 147, 오른쪽 369
# 가운데 열의 4개의 숫자 2,5,8,0은 현재 위치에서 더 가까거 사용
# 만약 거리가 같다면 오른손잡이느 오른쪽, 왼손잡이는 왼손 사용
# 번호에 따른 사용 손 출력

import sys
# sys.stdin=open("input.txt","r")


def solution(numbers, hand):

    a=[["1","2","3"],["4","5","6"],["7","8","9"],["*","0","#"]]


    # 왼손, 오른손의 시작 위치
    lh=[3,0]
    rh=[3,2]


    answer = ''

    # (0,0) (0,1) (0.2)
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)
    # abs(x2-x1) + abs(y2-y1)

    for num in numbers:
        # print("num",num)


        if num in (1,4,7) :
            answer+="L"

            # if str(num)=="1":
            for i in range(len(a)):
                for j in range(3):
                    if a[i][j]==str(num):
                        lh[0]=i
                        lh[1]=j
                        break


        elif num in  (3,6,9):

            answer+="R"

            for i in range(len(a)):
                for j in range(3):
                    if a[i][j]==str(num):
                        rh[0]=i
                        rh[1]=j
                        break


        #  그 외는 거리 계산
        else :
            lh_x,lh_y=lh[0],lh[1]
            rh_x,rh_y=rh[0],rh[1]

            for i in range(len(a)):
                for j in range(3):
                    if a[i][j]==str(num):


                        lh_distance=abs(lh_x-i)+abs(lh_y-j)
                        rh_distance=abs(rh_x-i)+abs(rh_y-j)

                        if lh_distance<rh_distance:
                            answer+="L"
                            lh[0],lh[1]=i,j

                        elif lh_distance>rh_distance:
                            answer+="R"
                            rh[0],rh[1]=i,j

                        else :
                            if hand=="left":
                                answer+="L"
                                lh[0],lh[1]=i,j

                            else :
                                answer+="R"
                                rh[0],rh[1]=i,j


                        break


    print(answer)



    return answer



# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
# solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	,"right")