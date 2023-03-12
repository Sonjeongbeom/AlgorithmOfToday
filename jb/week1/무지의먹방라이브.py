import heapq

def solution(food_times, k) :
    if sum(food_times) <= k :
        return -1

    queue = []
    for i, v in enumerate(food_times) :
        queue.append((v, i+1))
    heapq.heapify(queue)
    current = 0

    while queue and k :
        length = len(queue)
        if (queue[0][0] - current) * length <= k :
            root = heapq.heappop(queue)
            k -= (root[0] - current) * length
            current = root[0]
        else :
            break
    
    result = sorted(queue, key = lambda x : x[1])
    return result[k % len(queue)][1]