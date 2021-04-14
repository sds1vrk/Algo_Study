a=[5,3,1,7,8]
n=len(a)
print(a[n::-1])


for i in range(n-1,-1,-3):
    print(a[i],end=" ")
