# Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Python
```Python3
def generateParenthesis(N):
    res = []
    def cond_permut(S = '', left = 0, right = 0):
        if len(S) == 2*N:
            res.append(S)
            return
        if left < N:
            cond_permut(S +'(', left+1, right)
        if right < left:
            cond_permut(S +')',left,right+1)
    cond_permut()
    return res  
	
```