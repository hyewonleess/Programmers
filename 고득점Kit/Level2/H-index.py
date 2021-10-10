# my solution
def solution(citations):
    citations.sort()
    max_ = 0
    for h in range(max(citations)+1):
        up = [x for x in citations if x>=h] # h편이상 인용된 논문
        if h <= len(up):
            max_ = max(max_, h)
    return max_
  
  
# best solution 1
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
  

