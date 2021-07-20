# 추석 트래픽

def solution(lines):
    answer = 0

    total_times=[]


    # 1. 밀리초로 바꾸고 start_time과 end_time 구하기
    # 1시간 3600s ==> 밀리초 까지 ==> 3600 * 1000 ==> 360만
    # 1분 60s ==> 밀리초 까지 60 * 1000 ==> 6만
    def get_times(log):
        temp=log.split(" ")
        end_time=temp[1].split(":")
        # 360만
        end_time=int(end_time[0])*3600000+int(end_time[1])*60000+int(end_time[2].replace(".",""))
        start_time=end_time-int(float(temp[2].replace("s",""))*1000)+1

        print("start_time",start_time)
        print("end_time", end_time)

        return (start_time,end_time) if start_time>0 else (0,end_time)


    # 시작 시간 종료 시간 변경하기
    for i in range(len(lines)):
        start_time,end_time=get_times(lines[i])
        total_times.append((start_time,end_time,i))


    # 값 구하기
    # 끝나는 시간을 구하고 탐색하면서 다른 시작시작과, 종료시간에 들어가 있는지 확인하기
    for i in range(len(total_times)):
        count=1
        end_time=total_times[i][1]

        for j in range(len(total_times)):
            if i==j:
                continue

            t_start_time=total_times[j][0]
            t_end_time=total_times[j][1]

            if t_start_time >= end_time and t_start_time < end_time+1000:
                count+=1

            elif t_end_time>=end_time and t_end_time <end_time+1000:
                count+=1

            elif end_time>=t_start_time and end_time+1000<=t_end_time:
                count+=1

        if count>answer:
            answer=count


    return answer

solution( [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
])