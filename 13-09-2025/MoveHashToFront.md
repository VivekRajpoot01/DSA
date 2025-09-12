# Problem Statement

You are given a string that contains some `#` characters.  
Your task is to move all the `#` characters to the **front** of the string while keeping the relative order of the other characters the same.
### Example
##### Input: Move#Hash#To#The#Front
##### Output: ####MoveHashToTheFront

### Code
```python
def moveHashFront(s) ->str:
    result = ""
    count_hash = s.count('#')
    without_hash = s.replace('#','')
    result = '#'*count_hash + without_hash
    
    return result
    
s = input()
print(moveHashFront(s))
```
