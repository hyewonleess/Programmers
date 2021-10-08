# my solution
from collections import Counter

def solution(n, lost, reserve):
    s = [1]*n
    lost.sort()
    reserve.sort()

    c_re = list(Counter(reserve)-Counter(lost))
    c_lo = list(Counter(lost)-Counter(reserve))

    for i in c_re: s[i-1] = 2
    for i in c_lo: s[i-1] = 0

    dx = [-1, 1]

    for i in reserve:
        for j in  range(2):
            nx = (i-1) + dx[j]
            if 0<=nx<n and s[nx] == 0 and s[i-1]>1:
                s[nx] = 1
                s[i-1] = 1
    answer = len([i for i in s if i>0])
    return answer




# best solution
def solution(n, lost, reserve):
    _reserve = [r for  r in reserve if r not in lost]
    _lost = [l for l in reserve if l not in reserve]
    
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove()
        elif b in _lost:
            _lost.remove()
            
    return n-len(_lost)
