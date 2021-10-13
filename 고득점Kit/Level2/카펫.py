def solution(brown, yellow):
    n = brown+yellow
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            l = [n//i, i]
            if (l[0]*2+(l[1]-2)*2) == brown and (l[0]-2)*(l[1]-2) == yellow:
                answer = l
    return answer
