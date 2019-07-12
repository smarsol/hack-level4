def parells(nums):
  return [x for x in nums if x%2 == 0]

def mitjana(nums):
  N = 0
  for i in nums:
    N += i
  return(N/len(nums))

def variancia(nums):
  a = sum([((x-mitjana(nums))**2) for x in nums])
  return(a/len(nums))

nums = [1,2,5,7,9]

func_list = [mitjana,parells,variancia]

def apply_funcs(nums,func_list):
  results = []
  for n in func_list:
    results.append(n(nums))
  return results

print(apply_funcs(nums,func_list))
