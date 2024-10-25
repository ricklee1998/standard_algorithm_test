## 실패율 ##
"""
스테이지 개수 N 1~500
stages 길이 1~200000
stages 1~ N+1 이하의 자연수 존재
각 자연수는 사용자가 현재 도전 중인 스테이지 번호 나타남, N+1은 마지막 스테이지, 즉 N까지 클리어한 사용자 나타남
실패율이 같다면 작은 번호의 스테이지가 먼저 오면 된다
도달한 유저가 없는 경우 해당 스테이지의 실패율은 0
"""

#O(m + nlogn)
def solution(n, stages):
  #o(m)
  ppl = len(stages)
  cur_pl = ppl
  challenger = [0] * (n + 2)
  for stage in stages:
    challenger[stage] += 1
  fails = {} #dict
  for i in range(1, len(challenger)-1):
    fails[i] = challenger[i] / cur_pl
    cur_pl -= challenger[i]
  print(fails)
  #O(nlogn)
  result = sorted(fails, key=lambda x: fails[x], reverse=True)
  return result


N = 5
sts = [2,1,2,6,2,4,3,3]
#result = [3,4,2,1,5]


def solution2(N, stages):
  challenger = [0] * (N+2)
  for stage in stages:
    challenger[stage] += 1

  fails = {}
  total = len(stages)
  for i in range(1, N+1):
    if challenger[i] == 0:
      fails[i] = 0
    else:
      fails[i] = challenger[i] / total
      total -= challenger[i]
  print(fails)
  result = sorted(fails, key=lambda x: fails[x], reverse=True)
  return result
print(solution(N, sts))

