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
### Recrusive approach
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
### iterative approach
```
def generateParenthesis(self, n: int) -> List[str]:
    if n == 0
        return [""]
    res = ['('*n+')']
    for i in range(1,n): #insert ith right parenthesis
        for r in range(len(res)-1,-1,-1): # r: the rth answer after inserting i-1 right parenthesis.
            temp_res = []
    # the valid place to insert the i the parenthesis is on the right of the ith left parenthesis
    # and the first right parenthesis (from left to right).
            print(n-i-1,res[r].index(')'))
            for j in range(n-i-1,res[r].index(')')):
                temp_res.append(res[r][:j] + '()' + res[r][j+1:])
    # temp_res includes all combination after inserting the ith right parenthesis
            res[r:r+1] = temp_res
    return res
```