# 다시 풀어볼것!
def alpha_idx(alpha):
    a = ord(alpha)-65
    if  a <= 12:
        cnt = a
    else:
        cnt = 26 - a
    return cnt

def solution(name):
    answer = 0
    n=len(name)
    for i in range(n):
        if name[i]!='A':
            move=i
    for idx in range(n):
        if name[idx]!='A':
            answer+=alpha_idx(name[idx])
            next_idx=idx+1
            while next_idx<n and name[next_idx]=='A':
                next_idx+=1

            move=min(move,idx*2+n-next_idx)
    answer+=move
    return answer
