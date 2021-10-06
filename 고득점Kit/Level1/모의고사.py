# my solution
def solution(answers):
    n = len(answers)
    p1 = [1,2,3,4,5]
    p1 = p1*(n//len(p1)) + p1[:(n%len(p1))]
    p2 = [2,1,2,3,2,4,2,5]
    p2 = p2*(n//len(p2)) + p2[:(n%len(p2))]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    p3 = p3*(n//len(p3)) + p3[:(n%len(p3))]
    
    cnts = []
    for p in [p1, p2, p3]:
        cnt = 0
        for i in range(len(answers)):
            if p[i] == answers[i]:
                cnt += 1
        cnts.append(cnt)
        
    answer = [i+1 for i, x in enumerate(cnts) if x == max(cnts)]
    return answer
