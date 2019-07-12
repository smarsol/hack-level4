nums = [1,2,7,9,4,6]

def parells(nums):
  nums2 = []
  for n in nums:
    if n%2 == 0:
      nums2.append(n)
  return(nums2)

print(parells(nums))
