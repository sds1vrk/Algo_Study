# 등굣길

def solution(m, n, puddles):

    # 초기값
    x,y=1,1

    # print("m/n",m,n)
    array=[]
    for i in range(n):
        array.append([])
        for j in range(m):
            array[i].append(0)

    # print(array)

    array[0][1]=1
    array[1][0]=1

    # puddles 부분은 -1로 처리
    size=len(puddles)

    for k in range(size):
        x,y = puddles[k][0],puddles[k][1]
        array[y-1][x-1]=-1


    # print("puddle",array)





    for i in range(n):
        for j in range(m):


            # if temp[0]-1==i and temp[1]-1==j:
            #     continue

            if array[i][j]==-1:
                continue

            if i==0 and i<j:
                # print("array[i][j-1]+1",array[i][j-1],i,j)
                if array[i][j-1]==-1:
                    array[i][j]=array[i][j-1]

                else :
                    array[i][j] = 1


            elif j==0 and i>j:

                if array[i-1][j] == -1:
                    array[i][j] = array[i-1][j]

                else :
                    array[i][j]=1

            else :
                if array[i][j-1]==-1:
                    array[i][j] = array[i - 1][j]

                if array[i-1][j]==-1:
                    array[i][j] = array[i][j-1]

                if array[i-1][j]!=-1 and array[i][j-1]!=-1:
                    array[i][j] = array[i - 1][j] + array[i][j - 1]


    # print(array)

    answer = array[n-1][m-1]

    if answer==-1:
        answer=0

    else :
        answer=answer%1000000007
    # print(answer)
    return answer