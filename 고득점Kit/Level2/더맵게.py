import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        min_sc = heapq.heappop(scoville)
        if min_sc >= K:
            return answer
        else:
            min_sc2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_sc + min_sc2*2)
            answer += 1
    
    if scoville[0] >= K:
        return answer
    else:
        return -1
