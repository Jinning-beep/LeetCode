# 4Sum
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.


**Note:**

The solution set must not contain duplicate quadruplets.

Example:
```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## Python 
```Python 3
def fourSum(nums, target):
    nums.sort()
    length = len(nums)
    res = set()
    if length <= 3:
        return []
    if nums[0] + nums[1] + nums[2] + nums[3] > target or nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
        return []

    for i in range(0,length-3):
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            continue
        if  nums[length-1] + nums[length-2] + nums[length-3] + nums[i] < target:
            continue
        ### from here, the problem become a 3 sum problem    
        for j in range(i+1, length-2):
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                continue
            if nums[length-1] + nums[length-2] + nums[j] + nums[i] < target:
                continue

            left, right = j+1, length-1
            residual = target - nums[i] - nums[j]
            while left < right:
                sums = nums[left] + nums[right]
                # when sums = residual, then we have a new result
                if sums == residual:
                    res.add((nums[i],nums[j],nums[left],nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
					left += 1
					right -= 1
				# when the sums < residual, we move the left head to the right
				elif sums < residual:
						left += 1
				# when the sums > residual, we move the right head to the left.
				else:
					right -= 1
	return list(res)				
```