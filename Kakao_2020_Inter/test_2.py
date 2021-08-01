def solution(riddle):
    sol = ""
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cur_char = 0
    for i in range(len(riddle)):
        if riddle[i].isalpha():
            sol += riddle[i]
        else:
            if i > 0:
                if riddle[i - 1] == chars[cur_char]:
                    cur_char = (cur_char + 1) % 26

            if i < len(riddle) - 1:
                if chars[cur_char] == riddle[i + 1]:
                    cur_char = (cur_char + 1) % 26
                    if i > 0:
                        if chars[cur_char] == sol[i - 1]:
                            cur_char = (cur_char + 1) % 26
                    else:
                        cur_char = (cur_char + 1) % 26

            sol += chars[cur_char]
            cur_char = (cur_char + 1) % 26

    return sol


riddle = "ab?ac?"
print(solution(riddle))

riddle = "rd?e?wg??"
print(solution(riddle))

riddle = "????????"
print(solution(riddle))

