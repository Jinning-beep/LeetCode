# Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol  |      Value     |
|----------|:-------------:|
| I |  1 |
| V |   5   |
| X | 10 |
|L|50|
|C|100|
|D|500|
|M|1000|

For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X + II`. The number twenty seven is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

`I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
`X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
`C` can be placed before `D` (500) and `M `(1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
```
Input: "III"
Output: 3
```

Example 2:
```
Input: "IV"
Output: 4
```

Example 3:
```
Input: "IX"
Output: 9
```

Example 4:
```
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

Example 5:
```
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
##Python3
```
class Solution:
    def romanToInt(self, s: str) -> int:
		total, num_c,num_x, num_i = [0,0,0,0]
		for i in s:
			if i == 'M':
				if num_c == 0:
					total = total + 1000
				else:
					total = total + 1000 - 200
			if i == 'D':
				if num_c == 0:
					total = total + 500
				else:
					total = total + 500 - 200
			if i == 'C':
				num_c += 1
				if num_x == 0:
					total = total + 100
				else:
					total = total + 100 -20
			if i == 'L':
				if num_x == 0:
					total = total + 50
				else:
					total = total + 50 -20
			if i == 'X':
				num_x += 1
				if num_i == 0:
					total = total + 10
				else:
					total = total + 10 - 2
			if i == 'V':
				if num_i == 0:
					total = total + 5
				else:
					total = total + 5 - 2   
			if i == 'I':
				num_i += 1
				total = total + 1
		return total
```

```
class Solution:
    def romanToInt(self, s: str) -> int:
		roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
		res = 0
		for i in range(len(s)):
			if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
				res -= roman_dict[s[i]]
			else:
				res += roman_dict[s[i]]
		return res
```