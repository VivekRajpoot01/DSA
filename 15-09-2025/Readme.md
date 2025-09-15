# DSA Progress - Basic Problems

## 1. Check Palindrome

A palindrome is a number that reads the same forwards and backwards.

```python
def check_palindrome(n):
    num = n
    res = 0
    while num > 0:
        digit = num % 10
        res = res * 10 + digit
        num = num // 10
    
    return n == res

n = int(input())
print(check_palindrome(n))
```

**Algorithm:**
- Reverse the number by extracting digits from right to left
- Compare the reversed number with the original
- Time Complexity: O(log₁₀(n))
- Space Complexity: O(1)

---

## 2. Count Digits in a Number

Count the total number of digits in a given number.

```python
# Method 1: Using while loop
n = 5873
num = n  # creating new var so that it does not affect input variable 
count = 0
while num > 0:
    digit = num % 10
    count += 1
    num = num // 10
    
print(count)
# Time complexity: O(log₁₀(n)) as we are dividing constantly with 10

# Method 2: Using logarithm
from math import log10
res = int(log10(n) + 1)
print(res) 
```

**Algorithm:**
- **Method 1:** Keep dividing the number by 10 until it becomes 0
- **Method 2:** Use mathematical formula: digits = floor(log₁₀(n)) + 1
- Time Complexity: O(log₁₀(n)) for Method 1, O(1) for Method 2

---

## 3. Check Armstrong Number

An Armstrong number is a number that equals the sum of its digits raised to the power of the number of digits.

```python
def check_armstrong(n):
    num = n
    res = 0
    while(num > 0):
        digit = num % 10
        res = res + (digit**3)  # Assuming 3-digit Armstrong number
        num = num // 10
        
    return n == res

n = int(input())
print(check_armstrong(n))
```

**Algorithm:**
- Extract each digit and raise it to the power of total digits
- Sum all the powered digits
- Compare with original number
- Time Complexity: O(log₁₀(n))
- Space Complexity: O(1)

**Note:** This implementation assumes 3-digit numbers. For a complete solution, first count digits then use that count as power.

---

## 4. Print Factors of a Number

Find all factors of a given number using different approaches.

```python
n = 10

# Method 1: Brute Force - Check from 1 to n
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
# Time complexity: O(n)        

# Method 2: Optimized - Check from 1 to n//2 plus n itself
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(i)
print(n)    
# Time complexity: O(n/2) ≈ O(n) but fewer operations

# Method 3: Most Optimal - Check from 1 to √n
from math import sqrt
factors_list = []
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        factors_list.append(i)
        if(n // i != i):  # Avoid adding duplicate for perfect squares
            factors_list.append(n // i)

print(sorted(factors_list))
# Time complexity: O(√n)
```

**Algorithm Comparison:**
- **Brute Force:** Check every number from 1 to n
- **Optimized:** Check from 1 to n/2 + include n
- **Most Optimal:** Check from 1 to √n, add both i and n/i as factors

---

## 5. Hashing - Frequency Count

Using hashing to efficiently count occurrences and avoid Time Limit Exceeded (TLE) errors.

```python
# Problem: Count frequency of elements from array n in array m
m = [1, 2, 5, 6, 1, 2, 5, 7, 9]
n = [5, 2, 3, 9, 1]

# Without hashing: O(n*m) - Can cause TLE for large inputs
# With hashing: O(n+m) - Much more efficient

# Constraint: numbers are between 0 to 10
hash_list = [0] * 11  # Initialize frequency array

# Count frequencies in array m
for num in m:
    hash_list[num] += 1
    
# Query frequencies for array n
for num in n:
    print(hash_list[num])
```

**Algorithm:**
- Create a hash array of size (max_element + 1)
- Count frequency of each element in the first array
- Answer queries in O(1) time using the hash array
- Time Complexity: O(n + m) instead of O(n × m)
- Space Complexity: O(max_element)

**Key Advantage:** Reduces time complexity from O(n×m) to O(n+m), preventing TLE in competitive programming.

---

## Progress Summary

✅ **Completed Topics:**
1. Number manipulation (Palindrome, Digit counting)
2. Mathematical problems (Armstrong numbers)
3. Divisibility and factors
4. Basic hashing and frequency counting

📝 **Key Learning Points:**
- Time complexity optimization techniques
- Space-time trade-offs in algorithms
- Importance of hashing in competitive programming
- Mathematical approaches vs iterative approaches

