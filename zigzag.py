

<code>class Solution:
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
		\
		
		
		#
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
	</code>