def sum2(nums):
  if len(nums)>2:
    return nums[0] + nums[1]
  elif len(nums) == 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))