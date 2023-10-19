def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choosing a pivot element, you can choose any element but mostly the middle one is used
    left = [x for x in arr if x < pivot]  # list comprehension to add the left part of the list
    middle = [x for x in arr if x == pivot]  # Adding the pivot to its fixed position
    right = [x for x in arr if x > pivot]  # list comprehension to add the right part os the list

    return quick_sort(left) + middle + quick_sort(right)  # Recursively calling the function on the left and right list and returning the merged value.



my_list = [3, 6,2,18,19,17,99, 8, 10, 1, 2, 1]
sorted_list = quick_sort(my_list)
print(sorted_list)