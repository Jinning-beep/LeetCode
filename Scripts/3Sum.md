# 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

# Python 
## Python 3
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,pos,neg,zeros = [],{},{},0
        if not nums:
            return res
        for num in nums:
            if num > 0:
                pos[num] = 1 if not num in pos else pos[num]  + 1
            if num == 0:
                zeros += 1
            if num < 0:
                neg[num] = 1 if not num in neg else neg[num] + 1

        if zeros >= 3:
            res.append((0,0,0))
        if len(neg) == 0 or len(pos) == 0:
                    print([])
        if zeros > 0:
            for num in neg:
                if -num in pos:
                    res.append((num, 0, -num))
        for i, j in itertools.combinations_with_replacement(neg.keys(), 2):
            if i == j and neg[i] == 1:
                continue
            if -(i + j) in pos:
                res.append((i, j, -(i + j)))
        for i, j in itertools.combinations_with_replacement(pos.keys(), 2):
            if i == j and pos[i] == 1:
                continue
            if -(i + j) in neg:
                res.append((i, j, -(i + j)))
        return res
```