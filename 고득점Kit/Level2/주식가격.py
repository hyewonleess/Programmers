# my solution
def solution(prices):
    n = len(prices)
    answer = []
    for i, p in enumerate(prices[:-1]):
        sec = 0
        next_p = p
        while p <= next_p and i+sec < n-1:
            sec += 1
            next_p = prices[i+sec]
        answer.append(sec)
    answer.append(0)
    return answer
  
  
# best solution
def solution(prices):
  answer = [0]*len(prices)
  for i in range(len(prices)):
    for j in range(i+1, len(prices)):
      if prices[i] <= prices[j]:
        answer[i] += 1
      else:
        answer[i] += 1
        break
  return answer
