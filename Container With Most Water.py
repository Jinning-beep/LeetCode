#!/usr/bin/env python
# coding: utf-8

# # Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# Example 1
# ```
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# ```

# In[77]:


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,area,maxarea = 0,0,0
        j = len(height)-1
        while i!=j:
            if height[i] > height[j]:
                area = (j-i)*height[j]
                j -=1
            else:
                area = (j-i)*height[i]
                i += 1
            if maxarea < area: 
                maxarea = area
        return maxarea

