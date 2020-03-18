# First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
```
Input: [1,2,0]
Output: 3
```
Example 2:
```
Input: [3,4,-1,1]
Output: 2
```
Example 3:
```
Input: [7,8,9,11,12]
Output: 1
```

**Note:**

Your algorithm should run in O(n) time and uses constant extra space.




```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if nums == [1]: return 2
        if 1 in nums:
            for i in range(1,nums[-1]+2):
                print(i)
                if not i in nums:
                    return i
        else: return 1
```
		