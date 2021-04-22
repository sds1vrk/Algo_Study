# 아나그램
from collections import defaultdict
import sys
# sys.stdin=open("input.txt","r")

n=list(input())
n.sort()
m=list(input())
m.sort()

n_set=set(n)
m_set=set(m)

n_dict=dict()
for i in n_set:
    n_dict[i]=1

for i in n:
    # k는1
    k=n_dict[i]
    n_dict[i]=k+1

m_dict=dict()
for i in m_set:
    m_dict[i]=1

for i in m:
    # k는1
    k=m_dict[i]
    m_dict[i]=k+1


# print(n_dict)
# print(m_dict)

if n_dict==m_dict:
    print("YES")
else :
    print("NO")



