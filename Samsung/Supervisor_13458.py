import sys
# sys.stdin=open("13458.txt")


n=int(input())
a=list(map(int,input().split()))
# print(a)

main_super,bu_super=list(map(int,input().split()))
# print(main_super,bu_super)


ans=[]

for i in range(n):
    k=a[i]
    k=k-main_super

    if k<=0:
        ans.append([1,0])
        continue
    else :
        p=k%bu_super
        bu=k//bu_super

        if p==0:
            ans.append([1,bu])

        else :
            ans.append([1,bu+1])

# print(ans)
cnt=0

for i in ans:
    cnt+=sum(i)

print(cnt)
