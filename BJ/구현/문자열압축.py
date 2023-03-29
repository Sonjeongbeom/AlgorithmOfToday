def solution(s):
    answer = len(s)
    for length in range(1,len(s)//2+1):
        comp=''
        stack=[]
        i=0
        while True:
            end=i+length
            value=s[i:end]
            if len(stack)>0 and stack[-1]!=value:
                if len(stack)>=2:
                    comp+=str(len(stack))+stack[-1]
                else:
                    comp+=stack[-1]
                stack=[]
            stack.append(value)
            if end>=len(s):
                break
            i=end
        if len(stack)>=2:
            comp+=str(len(stack))+stack[-1]
        else:
            comp+=stack[-1]
            
        answer=min(answer,len(comp))
            
    return answer