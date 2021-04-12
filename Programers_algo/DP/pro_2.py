# 정수 삼각형
# 문제 해결방법
# 1. 2차원 리스트 만들기 - 이때 개수는 1,2,3,4 ... 비례해서 만들기
# 2. 분할하기, 맨 왼쪽과 오른쪽, 그리고 가운데
# 3. 가운데 값 중에서 최대값 고르기, 이는 현재 숫자를 기준으로 한다.
#  - 덧붙여 설명하자면, 받을라는 사람이 4행 2열 7이라면 7을 기준으로 한칸 위족(i-1)에서 j-1열, j열 중 가장 큰 숫자를 저장한다.
#  - 대각선으로 받기 떄문에 j-1, j를 해준다.
#  - 그리고 triangle에 현재 받을 수인 7을 더해준다.

print('''
         7
      3     8  
    8    1    0
  2    7    4    4
4   5    2    6    5 
''')


def solution(triangle):
    # 삼각형의 높이
    size=len(triangle)

    # 이전꺼를 담는 2차원 리스트
    array=[]
    for i in range(size):
        array.append([])
        for j in range(i+1):
            array[i].append(0)

    print(array)

    array[0][0]=triangle[0][0]
    array[1][0]=array[0][0]+triangle[1][0]
    array[1][1]=array[0][0]+triangle[1][1]

    for i in range(1,size):
        for j in range(i+1):
            # 맨 왼쪽
            if j==0:
                array[i][0]=array[i-1][j]+triangle[i][0]
                # print("array[i][0]",array[i][0])

            # 맨 오른쪽
            elif i==j:
                array[i][j]=array[i-1][j-1]+triangle[i][j]
                # print("array[i][j]", array[i][j])

            # 그 외에 가운데
            else :
                array[i][j]=max(array[i-1][j-1],array[i-1][j])+triangle[i][j]


    # 마지막 리스트 중에 제일 큰거 return
    answer=max(array[size-1])
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])