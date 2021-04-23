# DFS로 중복 순열 구하기
# 중복 순열은 트리가 n가지로 뻗어있다고 생각하면 됨

import sys
# sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
# n개의 수

la=0
def dfs(idx):
    global la
    if idx==m:
        # print("출력")
        la+=1
        for j in range(m):
            print(ch[j],end=" ")
        print()

    else :
        '''
                 D[0]=1
               /    \   /
1.여기에서 또 for문 이때는 ch[1]=1 로 채워지고 다 채워졌으니깐 출력 후 함수 종료
2. 다음 for 문 임 ==> ch[1]=2로 채워지고 다 채워졌으니깐 출력 후 함 수 종료
3. 마지막 for문 ==> ch[1]=3으로 채워지고 다 채웠으니깐 출력 후 함 수 종료
==> 여기 까지 하면 D[0]=1일때 끝 

                D[0]=2  (위에꺼 반복)

                D[0]=3  (위에꺼 반복) 
        '''

        for i in range(n):
            # 처음에 들어가는 ch[0]=1 or 2 or 3 이 각각 들어간다
            # ch[0]이 정해진 상태에서 dfs 돌리는 거임
            ch[idx] = i + 1
            dfs(idx+1)



# m은 자리수
# 1 1, 1 2, 1 3, 2 1, 2 2, 2 3
ch = [0] * (m)
a=[]
# for i in range(n):
#     a[i]=i+1
dfs(0)
print(la)