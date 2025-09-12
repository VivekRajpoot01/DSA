## Problem Statement –
Given a string containing consecutive repeating characters, compress the string such that each character is followed by the number of times it occurs consecutively. If a character occurs only once, keep it as is.

Example:

Input: aabbbbeeeeffggg → Output: a2b4e4f2g3

Input: abbccccc → Output: ab2c5


### CODE
```python
def reduce_string(s) ->str:
    res = ""
    count = 1
    
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            if count>1:
                res += s[i-1]+str(count)
            else:
                res += s[i-1]
            count = 1
                
    # to handle the last group of string
    if count>1:
        res+= s[-1]+str(count)
    else:
        res += s[-1]
    
    return res
    
#taking input
s = input()
print(reduce_string(s))
```
