#!/usr/bin/env python
# coding: utf-8

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# 
# Example 1
# ```
# Input: 121
# Output: true
# ```
# Example 2
# ```
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# ```
# 
# Example 3
# ```
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# ```
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 

# In[ ]:


# use integer:
def isPalindrome(x):
    str_x = list(str(x))
    str_x.reverse()
    return list(str(x)) == str_x
    


# In[70]:


def isPalindrome2(x):
    if x < 0:
        return False
    prod = 1
    res = 1
    final = 0
    initial_x = x
    while not prod + res == 0: 
        prod,res = divmod(x,10)
        final = 10*final + res
        x = prod
    return final//10 == initial_x


# In[71]:





# In[69]:





# In[46]:





# In[ ]:




