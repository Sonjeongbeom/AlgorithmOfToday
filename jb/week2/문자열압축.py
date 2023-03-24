def solution(word) :
    answers = []

    if len(word) == 1 :
        return 1
    
    for i in range(1, len(word) // 2 + 1) :
        unit = word[:i]
        cnt = 1
        tmp = ''
        for j in range(i, len(word), i) :
            if word[j:j+i] == unit :
                cnt += 1
            else :
                if cnt == 1 :
                    cnt = ''
                tmp += (str(cnt) + unit)
                cnt = 1
                unit = word[j:j+i]
        if cnt == 1 :
            cnt = ''
        tmp += (str(cnt) + unit)
        answers.append(len(tmp))
    return min(answers)

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
