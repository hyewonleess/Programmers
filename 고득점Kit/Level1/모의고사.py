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


# best solution
def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, ans in enumerate(answers):
        if ans == p1[idx%len(p1)]: # 나머지를 효율적으로 이용한 풀이
            score[0] += 1
        if ans == p2[idx%len(p2)]:
            score[1] += 1
        if ans == p3[idx%len(p3)]:
            score[2] += 1
    
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    
    return result
