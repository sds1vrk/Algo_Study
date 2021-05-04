import sys
# sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
a=[]
for i in range(n):
   a.append(int(input()))


left = 0
right = max(a)

while True:
    mid = (left + right) // 2
    n = sum([c // mid for c in a])
    if n == m:
        break
    right -= 1

print(mid)

