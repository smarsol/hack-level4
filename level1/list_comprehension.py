def mitjana(nums):
  N = 0
  for i in nums:
    N += i
  return(N/len(nums))

def variancia(nums):
  a = sum([((x-mitjana(nums))**2) for x in nums])
  return(a/len(nums))
