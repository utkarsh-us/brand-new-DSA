"""
# Problem Statement: Finding Perfect Square Roots in an Array

You are given an array of integers. Your task is to write a Python function to calculate the square root of each element in the array and represent the results as key-value pairs. The key will be the original array element, and the value will be the square root of the element if it is a perfect natural number square root; otherwise, the value will be "No perfect root."

Write a Python function `calculate_square_roots(arr)` that takes an array of integers as input and returns a dictionary where each key is an element from the input array, and the corresponding value is the square root of the element if it is a perfect natural number square root; otherwise, it is "No perfect root."

A perfect natural number square root is an integer square root, meaning the square root of a number should be an integer without any decimal part.

Your task is to implement the `calculate_square_roots` function to solve this problem efficiently. You can assume that the input array will contain at least one element.

Function Signature:
def calculate_square_roots(arr: List[int]) -> Dict[int, Union[int, str]]:
    pass

Input:
- A list `arr` (1 <= len(arr) <= 1000) containing integers. The elements of the array will be positive integers.

Output:
- A dictionary where each key is an element from the input array, and the corresponding value is the square root of the element if it's a perfect natural number square root; otherwise, it is "No perfect root."

Examples:

Example 1:
arr = [4, 9, 16, 25, 36]
calculate_square_roots(arr)
Output:
{4: 2, 9: 3, 16: 4, 25: 5, 36: 6}

Example 2:
arr = [7, 8, 10, 14]
calculate_square_roots(arr)
Output:
{7: 'No perfect root', 8: 2, 10: 'No perfect root', 14: 'No perfect root'}
"""


import math

def calculate_square_roots(arr):
    result = {}
    
    for num in arr:
        sqrt = math.sqrt(num)
        if sqrt.is_integer():
            result[num] = int(sqrt)
        else:
            result[num] = "No perfect root"
    
    return result

# Input array from the user
input_str = input("Enter the array elements separated by space: ")
input_array = [int(x) for x in input_str.split()]

square_roots = calculate_square_roots(input_array)

for num, root in square_roots.items():
    print(f"Number: {num}, Square Root: {root}")


"""
#output

Enter the array elements separated by space: 25 46 36 16 81
Number: 25, Square Root: 5
Number: 46, Square Root: No perfect root
Number: 36, Square Root: 6
Number: 16, Square Root: 4
Number: 81, Square Root: 9

"""
