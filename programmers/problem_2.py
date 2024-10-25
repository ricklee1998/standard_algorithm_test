## 배열 제어하기 ##
# set 사용 O(n)
# sort O(nlogn)
input_1 = [4,2,2,1,3,4]
def solution(lst):
  new_lst = list(set(lst))
  new_lst.sort(reverse=True)
  print(new_lst)
  return(new_lst)

solution(input_1)