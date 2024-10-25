## 두 개 뽑아서 더하기 

input_1 = [2,1,3,4,1]
# O(n^2logn^2)
def solution(arr):
  lst = []
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      lst.append(arr[i] + arr[j])
  #nlogn^2
  #set -> o(n)
  #lst -> o(n^2)
  # O(n^2logn^2)
  answer= sorted(set(lst))
  print(answer)
  return answer

solution(input_1)