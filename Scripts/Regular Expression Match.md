# Regular Expression Match
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
Example 2
```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

Example 3
```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

Example 4
```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
```


# Python
## Python 3
```
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}
        def dp(i,j):
            if (i,j) in memo: 
                return memo[(i,j)]
            if j == len(pattern): 
                return i==len(text)

            first = i < len(text) and pattern[j] in {text[i], '.'} # the result of dp(i,j)

            if j <= len(pattern) - 2 and pattern[j+1] == '*':
                # Scenario 1: zero char before * in pattern or S2: text contains multiple same chars in the patterns (before *)
                ans =  dp(i,j+2) or first and dp(i+1,j) 
            else: 
                ans = dp(i+1,j+1) and first
            memo[(i,j)] = ans
            return memo[i,j]
        return dp(0,0)
```