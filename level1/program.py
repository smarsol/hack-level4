nums = []
with open ("data.txt", "r") as f:
  for line in f:
    nums.append(int(line))

N = len(nums)

total = 0
for num in nums:
  total = total + num

mitjana = total/N
print(mitjana)

