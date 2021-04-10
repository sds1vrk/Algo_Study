# 2차원 리스트 생성과 접근/ 함수 만들기
# _ 1번당 [0]*3 을 실행 따라서 총 3번 실행
# 행열 표로 생각
a=[[0]*3 for _ in range(3)]
print(a)

# 2차원 리스트 접근
for x in a:
    for y in x:
        print(y,end="")
    print()


# 파이썬 함수는 여러개 값 return 가능
def add(a,b):
    c=a+b
    d=a-b
    return c,d
print(add(3,2))


def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

a=[12,13,7,9,19]
for x in a:
    if isPrime(x):
        print(x,end=" ")
