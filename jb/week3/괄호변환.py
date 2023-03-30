def solution(p) :
    answer = ''
    
    def check_if_correct(p) :
        stack = []
        for v in p :
            if stack and stack[-1] == '(' and v == ')' :
                stack.pop()
            else :
                stack.append(v)
        return len(stack) == 0

    def split_into_balanced(p) :
        cnt = 0
        for i, v in enumerate(p) :
            if v == '(' :
                cnt += 1
            else :
                cnt -= 1
            if cnt == 0 :
                return p[:i+1], p[i+1:]
    
    if p == '' :
        return ''
    
    u, v  = split_into_balanced(p)
    if check_if_correct(u) :
        answer = u + solution(v)
    else :
        answer = '(' + solution(v) + ')'
        for v in u[1:-1] :
            if v == '(' :
                answer += ')'
            else :
                answer += '('
        
    return answer

            

