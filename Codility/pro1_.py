# 조건에 맞는 숫자
from datetime import datetime
import sys
sys.stdin=open("input.txt","r")

def solution(S):

    # print(S)
    a=S.splitlines()
    # print(a)

    # print("a",a[0])

    # 조건 1
    def date(day):

        day_arr=list(map(int,day.split("-")))
        # print(day_arr)

        time1=datetime(day_arr[0],day_arr[1],day_arr[2])

        time2=datetime(1995,10,13)

        # print(time2-time1)

        diff=(time2-time1).days

        if diff<=0:
            return False

        else :
            return True



    # 조건 2
    def sizeCompare(size):

        if size<240000:
            return True

        else :
            return False

    # 조건 3
    def fileName(name):
        k=["zip","rar","tgz"]
        if name in k:
            return True

        else :
            return False


    cnt=0
    # 하나씩 비교
    for i in a:
        data=i.split()
        # print(data)

        day=data[0]
        size=int(data[1])
        name=data[2].split(".")[1]




        if date(day) and sizeCompare(size) and fileName(name):
            cnt+=1



    # print(cnt)
    return cnt











# s=input("")
solution("""1988-08-29        956 system.zip
1976-09-16     126976 old-photos.tgz
1987-02-03     118784 logs.rar
1961-12-04  703594496 very-long-filename.rar
1980-08-03          2 DELETE-THIS.TXT
2014-08-23        138 important.rar
2001-08-26     595968 MOONLIGHT-SONATA.FLAC
1967-11-30     245760 archive.rar
1995-10-13        731 file.tgz""")
# solution("['1988-08-29', '956', 'system.zip', '1976-09-16', '126976', 'old-photos.tgz', '1987-02-03', '118784', 'logs.rar', '1961-12-04', '703594496', 'very-long-filename.rar', '1980-08-03', '2', 'DELETE-THIS.TXT', '2014-08-23', '138', 'important.rar', '2001-08-26', '595968', 'MOONLIGHT-SONATA.FLAC', '1967-11-30', '245760', 'archive.rar', '1995-10-13', '731', 'file.tgz']")