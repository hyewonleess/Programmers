# my solution
from collections import deque

def solution(priorities, location):
    q = deque()
    idx_q = deque()
    p_list = []

    for idx, p in enumerate(priorities):
        q.append(p)
        idx_q.append(idx)

    while q and idx_q:
        nu = q.popleft()
        idx =  idx_q.popleft()
        max_val = max(q) if q else 0
        if nu < max_val: # 뒤에 nu 보다 큰 값이 하나라도 있으면
            q.append(nu) # 맨 뒤에 붙이기
            idx_q.append(idx)
        else:
            p_list.append(idx)

    answer = p_list.index(location)+1
    return answer
  
  
  # best solution
  def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
