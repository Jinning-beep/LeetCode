# Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

# Python3
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # assign chars to each num
        dict_num = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        final_list = []
        ele_str = []
        # choose chars in the dict_num without replacement
        i = 0
        for ele in digits:
            ele_str = dict_num[ele]
            if i == 0:
                final_list = ele_str
            else:
                final_list = tuple(''.join(sub) for sub in tuple(itertools.product(final_list,ele_str)))
            i += 1
        return final_list
```