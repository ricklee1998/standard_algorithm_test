def find_pair(arr, x):
  #시간 복잡도 -> O(n^2)
  #공간 복잡도 -> O(n)
  arr.sort()
  seen = set()
  result = []

  for num in arr:
    target = x - num
    if target not in seen and target in arr:
      result.append((num, target))
    seen.add(num)

  return result

def find_pair3(arr, x):
  #시간 복잡도 -> O(n)
  #공간 복잡도 -> O(n)
  seen = set()
  #O(n)
  arr_set = set(arr)
  result = []
  for num in arr:
    target = x - num
    # target in arr_set O(1)
    if target in arr_set and num <= target and (num, target) not in seen:
      result.append((num, target))
      seen.add((num, target))
  return result

def find_pair2(arr, x, n):
  #시간 복잡도 -> O(nlogn)
  #공간 복잡도 -> O(n)
  arr.sort()
  result = []
  left, right = 0, n-1 # 왼쪽, 오른쪽
  while left < right:
    temp = arr[left] + arr[right]
    if temp == x:
      result.append((arr[left], arr[right]))
      left += 1
    elif temp < x:
      left += 1
    else:
      right -= 1
  return result

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 결과 출력
pairs = find_pair3(arr, x)
#pairs = find_pair2(arr, x, n)
for pair in pairs:
  print(pair)