# Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
```
Input: "()"
Output: true
```
Example 2:
```
Input: "()[]{}"
Output: true
```
Example 3:
```
Input: "(]"
Output: false
```
Example 4:
```
Input: "([)]"
Output: false
```
Example 5:
```
Input: "{[]}"
Output: true
```

## Python
```Python3
class Solution:
    def isValid(self, s: str) -> bool:
    # convert parentheses to dictionaries
        dic_par = {value:c for c,value in enumerate('()[]{}',1)}
        l_par = []
        if s == '':
                return True
        for char in s:
            # if it is a left part, add it to list l_par
            if dic_par[char] % 2 == 1:
                l_par.append(char)
            elif l_par == []:
                return False
            elif dic_par[char] != dic_par[l_par[-1]] + 1:
                return False
            else:
                del l_par[-1]
        return l_par == []
```