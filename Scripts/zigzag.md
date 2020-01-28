# ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```

Example 1:
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

# Python 3
```python 3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        str_len = len(s)
        direction = 1
        index_row = 0
        index_i = 0
        split_str = [""]*(n+1)
        final_str = ""
        if n == 1 :
            final_str = s
        elif n == 2:
            for i in s:
                split_str[index_i % 2] = split_str[index_i % 2] + i
                index_i += 1
            final_str = split_str[0] + split_str[1] 
        else:
            for i in s:
                if direction == -1 and index_row == 1:
                    split_str[index_row] = split_str[index_row] + i
                    index_row = 0
                    direction = 1   
                elif index_row < n :
                    split_str[index_row] = split_str[index_row] + i
                    index_row = index_row + direction
                if index_row == n:
                    split_str[index_row] = split_str[index_row] + i
                    direction = -1
                    index_row = index_row + direction -1
            for index_row in range(0,n):
                final_str = final_str + split_str[index_row] 
        return final_str  
```
		
```python3		
class Solution:
    def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		
		res = [""] * numRows
		direction = 1
		row = 0
		for char in s:
			res[row] += char
			row += direction
			if row == 0 or row == numRows-1:
				direction *= -1
		return "".join(res)
```