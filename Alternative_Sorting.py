"""
Alternative Sorting
Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest and the second element is the smallest, the third element is the second largest and the fourth element is the second smallest, and so on.

Examples:

Input: arr[] = [7, 1, 2, 3, 4, 5, 6]
Output: [7, 1, 6, 2, 5, 3, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.
Input: arr[] = [1, 6, 9, 4, 3, 7, 8, 2]
Output: [9, 1, 8, 2, 7, 3, 6, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.
Expected Time Complexity: O(nlogn).
Expected Auxiliary Space: O(n)."""

class Solution:
    def alternateSort(self,arr):
        a = sorted(arr)
        i = 0
        j= len(arr)-1
        b = []
        while i<j:
            b.append(a[j])
            b.append(a[i])
            i+=1
            j-=1
        if len(arr)%2 != 0:
            b.append(a[i])
        return b

'''explaination

This Python code implements an Alternative Sorting function, where it rearranges a given array of distinct integers so that elements alternate between the largest and smallest values.

Explanation of the Code

class Solution:
    def alternateSort(self, arr):
        a = sorted(arr)                # Step 1: Sorts the array in ascending order
        i = 0                           # Pointer i starts at the beginning of the sorted array
        j = len(arr) - 1                # Pointer j starts at the end of the sorted array
        b = []                          # Initializes an empty list to store the result

        while i < j:                    # Step 2: Iterate until the pointers cross each other
            b.append(a[j])              # Append the largest unprocessed element to b
            b.append(a[i])              # Append the smallest unprocessed element to b
            i += 1                      # Move i one step right
            j -= 1                      # Move j one step left

        if len(arr) % 2 != 0:           # Step 3: If the array length is odd
            b.append(a[i])              # Append the middle element (left after i == j)

        return b                        # Return the reordered list
Steps in Detail
Sorting the Array:

The array arr is sorted into a new list a, which makes it easy to access the smallest and largest elements.
Two-Pointer Approach:

The pointers i and j are used to pick the smallest and largest elements alternately.
i starts at the beginning of a, pointing to the smallest element.
j starts at the end of a, pointing to the largest element.
In each iteration of the while loop:
The largest remaining element (a[j]) is appended to b.
The smallest remaining element (a[i]) is appended to b.
The pointers are updated (i moves right, j moves left) until they cross each other.
Handling Odd-Length Arrays:

If the array has an odd length, there will be a single middle element left after i and j meet. This middle element is appended to b at the end.
Result:

The final list b now contains elements arranged in the specified alternating order.'''
