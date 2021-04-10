# 4. While 문

# while True:
#     n, m = map(int, input().split())
#     if 0<n<10 and 0<m<10:
#         break
#     print(n+m)
import sys
while True:
    n,m=map(int,sys.stdin.readline().split())
    print(n+m)

print("test")