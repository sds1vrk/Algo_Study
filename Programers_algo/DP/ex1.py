# DP의 대표적인 예제는 피보나치 수열
# 피보나치 수열 : 1 1 2 3 5 8 13

# 재귀 함수를 사용하면 n이 커질수록 수행 시간이 기하급수적으로 늘어남
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

# 따라서 피보나치 수열을 메모제이션을 이용하여 한번 계산한 값을 저장함
d=[0]*100
# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo_dp(x):
    if x==1 or x==2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x]!=0:
        return d[x]

    # 아직 계산하지 않는 문제라면 점화식에 따라 피보나치 결과 반환
    # 이떄 메모제이션을 이용해서 한번 구한 값을 기록
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

d=[0]*100
d[1]=1
d[2]=1
def fibo_dp_for(n):
    # 피보나치 함수, 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]

    print(d[n])