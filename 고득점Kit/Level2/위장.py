# my solution
def solution(clothes):
    comb = {}
    for c in clothes:
        if c[1] not in comb:
            comb[c[1]] = [c[0]]
        else:
            comb[c[1]].append(c[0])

    answer = 1
    for c in comb.values():
        answer *= len(c)+1
    answer -= 1
    return answer
  
  
# best solution - Counter, reduce(집계함수, iterable 객체, initial)
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1)-1
    return answer
