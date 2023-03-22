def solution(n, build_frame):
    # 기둥 : 바닥 위, 보의 한쪽 끝부분 위, 다른 기둥의 위 (0)
    # 보 : 한쪽 끝 부분이 기둥, 양쪽 끝부분이 다른 보와 동시에 연결 (1)
    answers = set()
    def check() :
        # x 가로 좌표 / y 세로 좌표
        for x, y, a in answers :
            if a == 0 :
                if y != 0 and (x-1, y, 1) not in answers and (x, y, 1) not in answers and (x, y-1, 0) not in answers :
                    return False
            elif a == 1 :
                if (x, y-1, 0) not in answers and (x+1, y-1, 0) not in answers and ((x-1, y, 1) not in answers or (x+1, y, 1) not in answers) :
                    return False
        return True
            
    for x, y, a, b in build_frame :
        tmp = (x, y, a)
        if b == 1 :
            answers.add(tmp)
            if not check() :
                answers.remove(tmp)
        else :
            answers.remove(tmp)
            if not check() :
                answers.add(tmp)
    
    return sorted(list(answers), key = lambda x : (x[0], x[1], x[2]))