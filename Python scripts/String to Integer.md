
# String to Integer
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
*Only the space character ' ' is considered as whitespace character.
*Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1
```
Input: "   -42"
Output: -42
```
Example 2
```
Input: -123
Output: -321
```

Example 3
```
Input: "4193 with words"
Output: 4193
```

Example 4
```
Input: "words and 987"
Output: 0
```

Example 5
```
Input: "-91283472332"
Output: -2147483648
```


#Python 3
```
def myAtoi(Input_str):
    res = 0
    try:
        first_w = Input_str.split()[0]
    except:
        return res
    try:
        res = int(first_w)
    except:
        for i in range(1,len(first_w)):
            try: 
                res = int(first_w[:-i])
                break
            except:
                pass
    
    if res >= -2**31 and res <= 2**31 - 1:
        return res
    elif res < -2**31:
        return -2**31
    else:
        return 2**31 - 1        

```



