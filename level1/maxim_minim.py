nums = [2,3,45,6]

def mitjana(nums):
  N = 0
  for i in nums:
    N += i
  return(N/len(nums))

def variancia(nums):
  a = sum([((x-mitjana(nums))**2) for x in nums])
  return(a/len(nums))

def maxim(nums):
  if len(nums) == 0:
    return None
  maxim = nums[0]
  for n in nums:
    if maxim < n:
      maxim = n
  return(maxim)

def minim(nums):
  if len(nums) == 0:
    return None
  minim = nums[0]
  for n in nums:
    if minim > n:
      minim = n
  return(minim)

print(mitjana(nums))
print(variancia(nums))
print(maxim(nums))
print(minim(nums))
