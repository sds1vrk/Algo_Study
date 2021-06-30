import sys
import copy

# 첫번째 시도 ==> 시간초과
# 이유는 eval와 deepcopy사용으로 인한 시간 초과 발생
# 따라서 이 두개함수를 안쓰고 해결

# 문제 풀이 방법
# 1. 모든 경우의수를 확인하는 DFS (백트래킹)을 이용
# - 예를들어 + * 라면 모든 경우의 수 (*,+)와 (+,*)를 확인 : Permutation (순열)
# - 순열을 구하고 주어진


# 1. 숫자 및 배열 입력
sys.stdin=open("pro9.txt","r")
n=int(input())
a=list(map(int,input().split()))


# 2. 연산자 입력 및 개수대로 맞추기 operator
# + - X / 순서 및 개수 세기
op=list(map(int,input().split()))
default=["+","-","*","//"]
opers=[]
for i in range(len(op)):
    if op[i]!=0:
        for j in range(op[i]):
            opers.append(default[i])

print("opers",opers)
# 순열로 경우의 수 opers ! 구하기


# 최대값 및 최소값 미리 설정
max_value=-1e9
min_value=1e9


# ch는 연산자 넣을 공간
ch=[0]*len(opers)

# check는 해당 연산자 사용여부
check=[0]*(len(opers))

# DFS로 모든 경우의 수 구하기 연산자 개수 만큼 (예를들어 연산자가 3개라면 3!)
def dfs(l):
    global max_value
    global min_value
    if l==len(opers):
        # Deepcopy를 이용하면 속도 너무 증가됨
        # a=copy.deepcopy(a)

        # 나올수 있는 연산자
        for i in range(len(opers)):
            print(ch[i],  end=" ")
        print()

        res=a[0]
        b=a[1:]
        print("b",b)

        for i in range(len(b)):

            # 조건중에 앞에 숫자가 음수이고 %라면 - 취하고 다시 -붙이기
            if res<0 and ch[i]=="//":

                # eval도 속도 너무 많이 증가됨
                # value=eval(str(res)+ch[i]+str(b[i]))

                res=-1*res
                value=res//b[i]
                value=value*-1

            else :

                # eval도 속도 너무 많이 증가됨 ==> 삭제
                # value=eval(str(res)+ch[i]+str(b[i]))

                if ch[i]=="+":
                    value=res+b[i]
                elif ch[i]=="-":
                    value=res-b[i]
                elif ch[i]=="*":
                    value=res*b[i]
                elif ch[i]=="//":
                    value=res//b[i]

            res=value

        if res>max_value:
            max_value=res

        if res<min_value:
            min_value=res

    else :
        for i in range(len(opers)):
            # 백트래킹, DFS로 모든 경우의 수 세기
            # 만약 해당 연산자를 사용하지 않았으면 사용하고 방문처리 (check[i]==1)
            if check[i]==0:
                check[i]=1
                ch[l]=opers[i]
                dfs(l+1)

                # 다 사용했으면 다시 0으로 풀어주기, 그래야 다음 1부터 시작할떄 0을 다시 사용할 수 있기 때문에
                check[i]=0

dfs(0)

print(max_value)
print(min_value)