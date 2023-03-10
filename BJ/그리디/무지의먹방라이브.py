# 참고존나했음

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    arr=[]
    
    for i,food in enumerate(food_times):
        arr.append((food,i+1))
    
    arr.sort()
    
    length=len(arr)
    
    
    prev=0
    for i,food in enumerate(arr):
        diff=food[0]-prev
        value=diff*length
        
        if value<k:
            prev=food[0]
            k-=value
        else:
            k%=length
            
            newArr=sorted(arr[i:],key=lambda x:x[1])
            
            return newArr[k][1]
        
        length-=1
        
    return -1


print(solution([3,1,2],5))
print(solution([2,1,2],5))
print(solution([5,4,2,1],5))