# DSA Learning Progress - Recursion and Sorting Algorithms

This document contains implementations of fundamental Data Structures and Algorithms concepts including recursion problems and basic sorting algorithms.

## Table of Contents
1. [Recursion Problems](#recursion-problems)
   - [Factorial](#factorial)
   - [Array Reversal](#array-reversal)
   - [Fibonacci Sequence](#fibonacci-sequence)
2. [Sorting Algorithms](#sorting-algorithms)
   - [Selection Sort](#selection-sort)
   - [Bubble Sort](#bubble-sort)
   - [Insertion Sort](#insertion-sort)
3. [Complexity Analysis Summary](#complexity-analysis-summary)

---

## Recursion Problems

### Factorial

Finding the factorial of a number using recursion - a classic example of recursive thinking.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
```

**Explanation:**
- **Base Case:** When `n` is 0 or 1, return 1 (by definition, 0! = 1! = 1)
- **Recursive Case:** For any other number, multiply `n` by factorial of `(n-1)`
- **Example:** factorial(5) = 5 × 4 × 3 × 2 × 1 = 120

**Complexity Analysis:**
- **Time Complexity:** O(n) - We make n recursive calls
- **Space Complexity:** O(n) - Each recursive call uses stack space, creating a call stack of depth n

---

### Array Reversal

Reversing an array using recursion with two pointers approach.

```python
def reverse_array(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverse_array(nums, left + 1, right - 1)
```

**Explanation:**
- **Base Case:** When `left >= right`, we've reached the middle or crossed over
- **Recursive Case:** Swap elements at `left` and `right` positions, then move inward
- **Two Pointers:** `left` moves forward, `right` moves backward until they meet

**Complexity Analysis:**
- **Time Complexity:** O(n/2) ≈ O(n) - We process half the elements
- **Space Complexity:** O(n/2) ≈ O(n) - Recursive call stack depth is n/2

---

### Fibonacci Sequence

Computing the nth Fibonacci number using naive recursion.

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Explanation:**
- **Base Cases:** F(0) = 0, F(1) = 1
- **Recursive Case:** F(n) = F(n-1) + F(n-2)
- **Note:** This is an inefficient implementation due to repeated calculations

**Complexity Analysis:**
- **Time Complexity:** O(2^n) - Each call spawns two more calls, creating exponential growth
- **Space Complexity:** O(n) - Maximum depth of recursion tree is n

**Optimization Note:** This can be improved using dynamic programming or memoization to achieve O(n) time complexity.

---

## Sorting Algorithms

### Selection Sort

Sorts by repeatedly finding the minimum element and placing it at the beginning.

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
```

**Algorithm Steps:**
1. Find the minimum element in the unsorted portion
2. Swap it with the first element of the unsorted portion
3. Move the boundary of the sorted portion one step forward
4. Repeat until the entire array is sorted

**Complexity Analysis:**
- **Time Complexity:** O(n²) - Nested loops result in n(n+1)/2 comparisons
- **Space Complexity:** O(1) - Only uses a constant amount of extra space
- **Stability:** Not stable (equal elements may be reordered)

---

### Bubble Sort

Sorts by repeatedly stepping through the list and swapping adjacent elements if they're in wrong order.

```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        is_swap = False
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True
        if is_swap == False:
            return
```

**Algorithm Steps:**
1. Compare adjacent elements and swap if they're in wrong order
2. After each pass, the largest element "bubbles up" to its correct position
3. Use `is_swap` flag for early termination when array becomes sorted
4. Reduce the comparison range in each iteration

**Complexity Analysis:**
- **Time Complexity:** 
  - **Best Case:** O(n) - Array is already sorted, only one pass needed
  - **Average/Worst Case:** O(n²) - n(n+1)/2 comparisons
- **Space Complexity:** O(1) - Only uses constant extra space
- **Stability:** Stable (equal elements maintain their relative order)

---

### Insertion Sort

Builds the sorted array one element at a time by inserting each element into its correct position.

```python
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] >= key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
```

**Algorithm Steps:**
1. Start with the second element (index 1)
2. Store the current element as `key`
3. Shift all larger elements in the sorted portion to the right
4. Insert the `key` at its correct position
5. Repeat for all elements

**Complexity Analysis:**
- **Time Complexity:** O(n²) - In worst case, we compare with all previous elements for each element
- **Space Complexity:** O(1) - Only uses constant extra space
- **Stability:** Stable sorting algorithm

---

## Complexity Analysis Summary

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stable |
|-----------|-----------|--------------|------------|------------------|--------|
| **Recursion Problems** |
| Factorial | O(n) | O(n) | O(n) | O(n) | - |
| Array Reverse | O(n) | O(n) | O(n) | O(n) | - |
| Fibonacci (Naive) | O(2^n) | O(2^n) | O(2^n) | O(n) | - |
| **Sorting Algorithms** |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |

## Key Takeaways

### Recursion
- Always define clear base cases to avoid infinite recursion
- Consider the call stack depth for space complexity
- Some recursive solutions can be optimized using dynamic programming

### Sorting Algorithms
- **Selection Sort:** Simple but inefficient, performs the same number of comparisons regardless of input
- **Bubble Sort:** Can be efficient for nearly sorted arrays due to early termination
- **Insertion Sort:** Efficient for small arrays and nearly sorted data

### Next Steps for Learning
1. Implement optimized Fibonacci using memoization or iterative approach
2. Learn more efficient sorting algorithms (Merge Sort, Quick Sort, Heap Sort)
3. Practice more complex recursion problems (Tree traversals, backtracking)
4. Study space-time tradeoffs in algorithm design
