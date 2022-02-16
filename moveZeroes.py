# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


def moveZeroes(nums):
  zeros = []
  notZeros = []
  for num in nums:
    if num == 0:
      zeros.append(num)
    else:
      notZeros.append(num)
  
  c = 0
  for el in notZeros:
    nums[c] = el
    c += 1
  for el in zeros:
    nums[c] = el
    c += 1
  
  
A = [0, 1, 0, 3, 12]
moveZeroes(A)
print(A)
