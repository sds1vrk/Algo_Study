# 리스트와 내장함수(2)

# enumerate (인덱스 번호와 value 출력)
a=[23,12,36,53,19]
for x in enumerate(a):
    print(x)

# 튜플, 튜플은 리스트와 비슷, 다른점은 값을 변경 할 수 없음
b=(1,2,3,4,5)
print(b)

for x in enumerate(a):
    print(x[0],x[1])
print()
# enumerate 활용
for index,value in enumerate(a):
    print(index,value)

# all  모두 참일때 True, 하나라도 거짓이면 False
if all(50>x for x in a) :
    print("Yes")
else :
    print("No")

# any는 한번이라도 참이면 True, 모두다 거짓이면 False
if any(50>x for x in a) :
    print("Yes")
else :
    print("No")