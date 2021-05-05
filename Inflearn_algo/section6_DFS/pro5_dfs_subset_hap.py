# 부분집합의 합 구하기
# 앞에 구한 부분집합의 응용
# 체크 여부 ch를 개수 만큼 만들어주고
# 여기에 인덱스 번호를 넘겨주어 풀이, 그리고 ch에는 내가 들어 있는 값이 들어있음
# ch[1]=1, ch[2]=3, ch[3]=5 ...
# 각 경우당 dfs를 2번 호출 ==> 들어있냐, 안들어있냐! 이게 중요


import sys
sys.stdin=open("input.txt","r")
result=[]
def dfs(idx):
    if idx==n:
        hap=0
        # 부분집합의 모든 합을 구하고 처음과 끝을 비교
        for i in range(n+1):
            if ch[i]!=0:
                print(ch[i],end=" ")
                hap+=ch[i]
        result.append(hap)
        print()

    else :
        ch[idx+1]=m[idx]
        dfs(idx+1)
        ch[idx+1]=0
        dfs(idx+1)


n=int(input())
m=list(map(int,input().split()))
ch=[0]*(n+1)
idx=0
dfs(idx)

print(result)
# 처음과 끝을 비교
for i in range(len(result)//2):
    if result[i]==result[len(result)-1-i]:
        print("YES")
        break
else :
    print("NO")
