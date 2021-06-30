# 동전 분배하기
# 상태 트리 구현
# 0번, 1번, 2번 사람 ==> for 0,1,2
#
import sys
# sys.stdin=open("3190.txt","r")

n=int(input())
coin=[]
m=[0 for _ in range(3)]
# print(m)
for _ in range(n):
    coin.append(int(input()))

# print(coin)
res=99999999999999999999
def dfs(l):
    global res
    if l==len(coin):

        # 방법 1
        # a,b,c=m[0],m[1],m[2]
        # if a!=b and a!=c:
        #     if b!=c:
        #         kk=max(m)-min(m)
        #         if kk<=res:
        #             res=kk


        # 방법 2 ==> SET을 이용한 방법
        # set에 동전을 넣어주고 길이가 3일때만 대입시켜주는 방법
        kk=max(m)-min(m)
        if kk<res:
            tmp=set()
            for x in m:
                tmp.add(x)
            if len(tmp)==3:
                res=kk




    else :
        for i in range(3):
            # 돈을 더했던것을 빼줘야 함
            m[i]=m[i]+coin[l]
            dfs(l+1)
            m[i]=m[i]-coin[l]

dfs(0)
print(res)