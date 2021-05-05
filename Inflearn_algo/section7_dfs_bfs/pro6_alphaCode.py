# 알파코드
import sys
# sys.stdin=open("input.txt","r")


def dfs(l,p):
    global cnt
    if l==size:
        cnt+=1
        # positon 바로 전까지 뽑으면 됨
        for i in range(p):
            # print(chr(res[i]))
            print(chr(res[i]+64),end="")

        print()

    else :
        for i in range(1,27):
            # 가지치기
            if code[l] ==i:

                res[p]=i
                dfs(l+1,p+1)

            # i가 2자리 수이고
            elif i>=10 and i//10==code[l] and i%10==code[l+1]:
                res[p]=i
                dfs(l+2,p+1)


n=input()

k = int(n)
# print(k)
cnt=0
code=[]
for i in n:
    code.append(int(i))

# for문이 26까지만 돌기 때문에 마지막 인덱스가 2이하인 수에서는 에러가 난다, 이유는 마지막 인덱스가 없기 때문에
# 따라서 마지막 인덱스에 -1을 넣어 인덱스 에러를 방지

# print(code)
res=[]
size=len(n)
code.insert(size,-1)
for _ in range(len(n)):
    res.append(0)

dfs(0,0)

print(cnt)
# print(res)
# print(size)