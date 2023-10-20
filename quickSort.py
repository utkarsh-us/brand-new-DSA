'''
Problem Statement
You are given an unsorted list of integers. Your task is to implement the Quick Sort algorithm to sort the list in ascending order.

Write a Python function quick_sort(arr) that takes an unsorted list arr of integers and returns a new list with the same elements sorted in ascending order using the Quick Sort algorithm. Your function should not modify the original list but create and return a new sorted list.

Your implementation should be based on the Quick Sort algorithm and should have a time complexity of O(n log n) on average.
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choosing a pivot element, you can choose any element but mostly the middle one is used
    left = [x for x in arr if x < pivot]  # list comprehension to add the left part of the list
    middle = [x for x in arr if x == pivot]  # Adding the pivot to its fixed position
    right = [x for x in arr if x > pivot]  # list comprehension to add the right part os the list

    return quick_sort(left) + middle + quick_sort(right)  # Recursively calling the function on the left and right list and returning the merged value.


list = []  # Initialising an empty list

while True:  # A loop to add values in the empty list
    user_input = input("Enter a number (or 'x' to finish): ")  # Enter a number

    if user_input.lower() == 'x':  # Adding a break condition to exit the loop
        break

    try:   # Using try and exception to finally append the number in the list
        number = int(user_input)
        list.append(number)
    except ValueError:  # Except is used in case the user inputs some string or other invalid characters.
        print("Invalid input. Please enter a valid number or 'x' to finish.")

sorted_list = quick_sort(list)
print("Sorted list:", sorted_list)