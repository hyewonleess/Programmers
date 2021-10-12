# bfs
from collections import deque

def solution(numbers, target):
    q = deque([(0, 0)]) # sum, level
    answer = 0
    while q:
        sums, level = q.popleft()
        if level > len(numbers):
            break
        elif level == len(numbers) and sums == target:
            answer += 1
        q.append((sums+numbers[level-1], level+1))
        q.append((sums-numbers[level-1], level+1))
    return answer
