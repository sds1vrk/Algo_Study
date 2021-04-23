# 람다함수
# 익명의 함수, 표현식
def plus(x):
    return x+1
print(plus(2))

# 람다함수로 변경
# 변수명=람다
plus_two=lambda x:x+2
print(plus_two(1))

a=[1,2,3]
print(list(map(plus,a)))

# 리스트와 람다함수 혼합
print(list(map(lambda x:x+1,a)))