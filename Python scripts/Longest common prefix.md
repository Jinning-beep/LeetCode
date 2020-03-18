# Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
```
Input: ["flower","flow","flight"]
Output: "fl"
```

Example 2:
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Note:

All given inputs are in lowercase letters a-z.


# Python 3

```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs:
            return ''
        num_items = len(strs)
        pre = strs[0]
        for i in range(1,num_items):
            while not strs[i].startswith(pre):
                pre = pre[:-1]
        return pre
```