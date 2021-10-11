from collections import Counter
def solution(progresses, speeds):
    days = []
    for i, j in zip(progresses, speeds):
        days.append((99-i)//j+1)
    
    for i in range(len(days)-1):
        if days[i] >= days[i+1]:
            days[i+1] = days[i]
        
    answer = list(Counter(days).values())
    return answer
