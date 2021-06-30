# 세워라 반석위에
import sys
sys.stdin=open("21967.txt","r")

n=int(input())
a=list(map(int,input().split()))

# print(n)
# print(a)

lt=0

ans=[]
while lt<n:

    for rt in range(lt+1,n):
        if abs(a[lt]-a[rt])==2:
            # print("here")
            # print(a[lt:rt])

            if rt==n-2 and a[rt+1]==a[lt]:
                # print("ere")
                # ans.append(a[lt:rt+2])
                ans.append(len(a[lt:rt+2]))
                break

            else :
                ans.append(len(a[lt:rt+1]))
                # ans.append(a[lt:rt+1])

    print(ans)
    lt+=1


    # if ans.

# print(ans)
# print(len(max(ans)))
# print(max(ans))