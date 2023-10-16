"""Sure, here's a unique basic Python data structure question related to arrays:

**Question:** 
You are given an array of integers, where each element appears exactly twice except for one element, which appears only once. Write a Python function to find the element that occurs only once.

**Example:**

```python
Input: [4, 2, 3, 4, 3]
Output: 2

Input: [9, 7, 9, 8, 8]
Output: 7
```

**Explanation:**
In the first example, all elements except 2 appear twice, so the function returns 2. In the second example, all elements except 7 appear twice, so the function returns 7.

This question tests the candidate's understanding of array manipulation and knowledge of XOR operations, which can be used to efficiently find the element that appears only once."""


# solution

def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
nums = [4, 2, 3, 4, 3]
print(find_single_number(nums))  # Output: 2

nums = [9, 7, 9, 8, 8]
print(find_single_number(nums))  # Output: 7

"""I solved the "Single Number" problem using the XOR operation. Here's a step-by-step explanation of how the solution works:

1. Initialize a variable `result` to 0. This variable will be used to keep track of the unique element that occurs only once.

2. Iterate through the elements of the input array `nums` using a for loop.

3. In each iteration, perform a bitwise XOR operation between the current element `num` and the `result`. Here's why this works:
   - XORing the same number twice results in 0: `num ^ num = 0`.
   - XORing any number with 0 results in the number itself: `num ^ 0 = num`.

4. As you iterate through the array, the duplicates will cancel each other out due to the properties of the XOR operation. Only the unique element that occurs only once will remain in the `result` variable.

5. After processing all elements in the array, the `result` variable will contain the unique element.

6. Return the `result` as the output of the function.

The key insight here is that XORing a number with itself results in 0, and XORing a number with 0 gives the number itself. Therefore, XORing all elements in the array will leave you with the unique element that occurs only once, as it doesn't have a duplicate to cancel it out."""
