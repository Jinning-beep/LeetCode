# 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

# Python
## Python 3
```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('Inf')
        for start in range(len(nums)-2):
            min_sum = nums[start] + nums[start+1] + nums[start+2]
            max_sum = nums[-1] + nums[-2] + nums[start]
            if target <= min_sum:
                if abs(min_sum-target) < abs(res-target):
                    res = min_sum
                return res
            if target >= max_sum:
                if abs(max_sum-target) < abs(res-target):
                    res = max_sum
                continue

            mid = start + 1
            end = len(nums)-1
            while mid < end:
                sum_three = nums[start] + nums[mid] + nums[end]
                if abs(sum_three-target) <= abs(res-target):
                    res = sum_three
                if sum_three < target:
                    mid += 1
                elif sum_three == target:
                    return sum_three
                elif sum_three > target:
                    end -= 1
        return res
```